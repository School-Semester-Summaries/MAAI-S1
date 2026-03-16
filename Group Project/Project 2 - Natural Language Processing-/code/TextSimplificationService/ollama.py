import dspy
import argparse
import pandas as pd
import time
import re
from pathlib import Path

import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry

from markdown_loader import process_all_markdown_files

class QA(dspy.Signature):
  question = dspy.InputField()
  answer = dspy.OutputField()

embedding_model = get_registry().get("sentence-transformers").create(
    name="NetherlandsForensicInstitute/robbert-2022-dutch-sentence-transformers"
)

class Document(LanceModel):
    text: str = embedding_model.SourceField()
    vector: Vector(embedding_model.ndims()) = embedding_model.VectorField()
    source: str
    section_path: str

class RAG():
    def __init__(self, db_name):
        self.db_name = db_name
        self.db = None
    
    def __enter__(self):
        self.db = lancedb.connect(self.db_name)
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False
    
    def create_table(self, table_name, schema, data):
        assert self.db != None, "database not instantiated"

        if table_name in self.db.table_names():
            self.db.drop_table(table_name)

        return self.db.create_table(table_name, schema=schema, data=data)
    
    def load_markdown_directory(self, table_name, markdown_dir):
        """Load all markdown files from a directory into the database."""
        documents = process_all_markdown_files(markdown_dir)

        data = [
            {
                "text": doc["text"],
                "source": doc["source"],
                "section_path": doc["section_path"],
            }
            for doc in documents
        ]
        
        return self.create_table(table_name, schema=Document, data=data)

    def search(self, table_name, query, limit=3):
        assert self.db != None, "database not instantiated"
       
        table = self.db.open_table(table_name)

        return table.search(query).limit(limit).to_pandas()

class Model():
    def __init__(self, model, api_base, api_key, temperature):
        self.lm = dspy.LM(
            model=model,
            api_base=api_base,
            api_key=api_key,
            temperature=temperature,
            cache=False
        )

        # Configure ONCE
        dspy.configure(lm=self.lm)

        # Reuse predictor
        self.predictor = dspy.Predict(QA)

    def __call__(self, prompt):
        return self.predictor(question=prompt)



def read_prompts_from_file(file_path: str) -> list[str]:
    """Read prompts from a text file, one prompt per line."""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Filter out empty lines and strip whitespace
    return [line.strip() for line in lines if line.strip()]


def load_wordlists(wordlist_dir: str = "dataset/wordlists") -> dict:
    """Load all CSV wordlists from the directory into a dictionary.
    Returns a dict mapping words to their alternatives.
    """
    wordlist_path = Path(wordlist_dir)
    word_alternatives = {}
    
    if not wordlist_path.exists():
        print(f"Warning: Wordlist directory '{wordlist_dir}' not found.")
        return word_alternatives
    
    for csv_file in wordlist_path.glob("*.csv"):
        try:
            df = pd.read_csv(csv_file, encoding="utf-8")
            # Expect columns: woord, suggestie_1, suggestie_2, ...
            if "woord" not in df.columns:
                continue
            
            for _, row in df.iterrows():
                word = str(row["woord"]).strip().lower()
                if not word or word == "nan":
                    continue
                
                # Collect all suggestions
                suggestions = []
                for col in df.columns:
                    if col.startswith("suggestie"):
                        val = row[col]
                        if pd.notna(val) and str(val).strip():
                            suggestions.append(str(val).strip())
                
                if suggestions:
                    # Merge with existing suggestions if word already exists
                    if word in word_alternatives:
                        existing = word_alternatives[word]
                        for s in suggestions:
                            if s not in existing:
                                existing.append(s)
                    else:
                        word_alternatives[word] = suggestions
        except Exception as e:
            print(f"Warning: Could not load wordlist {csv_file}: {e}")
    
    print(f"Loaded {len(word_alternatives)} words with alternatives from wordlists.")
    return word_alternatives


def find_alternatives_in_sentence(sentence: str, word_alternatives: dict) -> list[tuple]:
    """Find words in the sentence that have alternatives.
    Returns a list of tuples: (original_word, [alternatives])
    """
    found = []
    # Tokenize sentence into words (keeping original case for display)
    words = re.findall(r'\b[\w-]+\b', sentence.lower())
    
    # Check each word and also check multi-word phrases
    sentence_lower = sentence.lower()
    
    # First check multi-word phrases (longer matches first)
    checked_phrases = set()
    for phrase in sorted(word_alternatives.keys(), key=len, reverse=True):
        if ' ' in phrase and phrase in sentence_lower and phrase not in checked_phrases:
            found.append((phrase, word_alternatives[phrase]))
            checked_phrases.add(phrase)
    
    # Then check individual words
    for word in words:
        if word in word_alternatives and word not in checked_phrases:
            found.append((word, word_alternatives[word]))
    
    return found


def create_rag_prompt(context: str, prompt: str, alternatives: list[tuple] = None) -> str:
    alternatives_section = ""
    if alternatives:
        alternatives_lines = []
        for word, suggestions in alternatives:
            suggestions_str = ", ".join(suggestions)
            alternatives_lines.append(f"- '{word}' → {suggestions_str}")
        alternatives_section = f"""
        
        Potentiële woordalternatieven die je kunt gebruiken:
        {chr(10).join(alternatives_lines)}
        """
    
    return f"""Je bent een assistent die teksten herschrijft naar eenvoudiger Nederlands (B1 niveau).
    
        Gebruik de volgende richtlijnen om de tekst te herschrijven:
        {context}
        {alternatives_section}
        Herschrijf de volgende tekst volgens bovenstaande richtlijnen:
        {prompt}

        Geef uitsluitend de herschreven tekst, zonder uitleg.
        """

def process_single_prompt(prompt: str, rag: RAG, model: Model, word_alternatives: dict = None) -> dict:
    # Augment the query to better match guidelines
    search_query = f"Hoe kan ik deze zin vereenvoudigen naar B1 niveau: {prompt}"
    
    results = rag.search("documents", search_query, limit=5)
    context = "\n\n".join(results['text'].tolist())
    
    # Find alternative words in the sentence
    alternatives = []
    if word_alternatives:
        alternatives = find_alternatives_in_sentence(prompt, word_alternatives)
    
    rag_prompt = create_rag_prompt(context, prompt, alternatives)
    
    start_time = time.time()
    response = model(prompt=rag_prompt)
    end_time = time.time()
    
    generation_time = end_time - start_time
    
    return {
        "original": prompt,
        "simplified": response.answer,
        "generation_time": generation_time,
        "alternatives_found": len(alternatives),
    }


def process_prompts(prompts: list[str], rag: RAG, model: Model, word_alternatives: dict = None, timing_file: str = "timing_results.txt") -> pd.DataFrame:
    """Process multiple prompts and return results as a DataFrame."""
    results = []
    total_time = 0.0
    
    for i, prompt in enumerate(prompts):
        print(f"Processing prompt {i + 1}/{len(prompts)}: {prompt[:50]}...")
        result = process_single_prompt(prompt, rag, model, word_alternatives)
        total_time += result["generation_time"]
        print(f"  Generation time: {result['generation_time']:.2f}s | Alternatives found: {result['alternatives_found']}")
        results.append(result)
    
    avg_time = total_time / len(prompts) if prompts else 0
    print(f"\nAverage generation time per prompt: {avg_time:.2f}s")
    print(f"Total generation time: {total_time:.2f}s")
    
    # Save timing results to txt file
    with open(timing_file, "w", encoding="utf-8") as f:
        f.write(f"Timing Results\n")
        f.write(f"==============\n\n")
        f.write(f"Number of prompts: {len(prompts)}\n")
        f.write(f"Total generation time: {total_time:.2f}s\n")
        f.write(f"Average generation time per prompt: {avg_time:.2f}s\n\n")
        f.write(f"Individual prompt times:\n")
        for i, result in enumerate(results):
            f.write(f"  Prompt {i + 1}: {result['generation_time']:.2f}s\n")
    print(f"Timing results saved to {timing_file}")
    
    return pd.DataFrame(results)

def save_results(df: pd.DataFrame, output_path: str):
    """Save the results DataFrame to a parquet file."""
    df.to_parquet(output_path, index=False)
    print(f"Results saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Required
    parser.add_argument("--prompt", required=False, default=None, 
                        help="Direct prompt text to process")
    parser.add_argument("--input-file", required=False, default=None,
                        help="Path to a .txt file containing prompts (one per line)")
    parser.add_argument("--output", required=False, default="results.parquet",
                        help="Output parquet file path (default: results.parquet)")

    # Not required
    parser.add_argument("--model", required=False, default="ollama_chat/granite3.3:2b")
    parser.add_argument("--api-base", required=False, default="http://localhost:11434")
    parser.add_argument("--api-key", required=False, default="")
    parser.add_argument("--temperature", required=False, default=None, type=float)
    
    args = parser.parse_args()

    # Validate input arguments
    if args.prompt is None and args.input_file is None:
        parser.error("Either --prompt or --input-file must be provided")
    
    if args.prompt is not None and args.input_file is not None:
        parser.error("Cannot use both --prompt and --input-file at the same time")

    model_name = args.model
    api_base = args.api_base
    api_key = args.api_key
    temperature = args.temperature
    output_path = args.output

    # Get prompts from direct input or file
    if args.input_file:
        prompts = read_prompts_from_file(args.input_file)
        print(f"Loaded {len(prompts)} prompts from {args.input_file}")
    
    else:
        prompts = [args.prompt]

    # Initialize model
    model = Model(model=model_name, api_base=api_base, api_key=api_key, temperature=temperature)
    
    # Load wordlists for alternative suggestions
    word_alternatives = load_wordlists("dataset/wordlists")

    with RAG(db_name="my_database") as rag:
        # Rebuild lanceDB (ONLY if it doesnt exist yet)
        if "documents" not in rag.db.table_names():
            rag.load_markdown_directory("documents", "markdown")
        
        # Process all prompts
        results_df = process_prompts(prompts, rag, model, word_alternatives)
    
    # Save results to parquet
    save_results(results_df, output_path)
    
    for idx, row in results_df.iterrows():
        print("")
        print(f"Original: {row['original']}")
        print(f"Simplified: {row['simplified']}")