# De REST-Controller
import subprocess
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from ollama import process_single_prompt, RAG, Model, load_wordlists
from evaluate import calculate_readability

# Flask app setup
# ---------------------------------------------------------------

app = Flask(__name__)
CORS(app)


print("⚙️  Initializing model...")
# Model (loaded once)
model = Model(
    model="ollama_chat/granite3.3:2b",
    api_base="http://localhost:11434",
    api_key="",
    temperature=None
)
print("⚙️  Warming up LM...")
model("Hallo, dit is een testzin om het model te warmen.")

print("⚙️  Loading spaCy...")
calculate_readability("Check!")

print("⚙️  Loading Wordlists...")
# Wordlists (loaded once)
word_alternatives = load_wordlists("dataset/wordlists")

print("⚙️  Setting up RAG...")
# RAG / LanceDB (opened once)
rag = RAG(db_name="my_database")
rag.__enter__()

# Build LanceDB only if needed
if "documents" not in rag.db.table_names():
    print("⚙️  Building LanceDB index...")
    rag.load_markdown_directory("documents", "markdown")

# Endpoints
# ---------------------------------------------------------------

# Zin versimpelen endpoint
@app.route("/prompt", methods=["POST"])
def prompt():
    data = request.get_json()
    if not data or "sentence" not in data:
        return jsonify(error="Missing 'sentence'"), 400

    sentence = data["sentence"]

    try:
        # 1. Simplify sentence
        result = process_single_prompt(
            sentence,
            rag=rag,
            model=model,
            word_alternatives=word_alternatives
        )

        simplified = result["simplified"]

        # 2. Evaluate readability
        original_scores = calculate_readability(sentence)
        simplified_scores = calculate_readability(simplified)

        improvement = None
        if original_scores["lint_score"] is not None and simplified_scores["lint_score"] is not None:
            improvement = original_scores["lint_score"] - simplified_scores["lint_score"]

        # 3. Build response JSON
        response = {
            "original": {
                "sentence": sentence,
                "valid": original_scores["lint_score"] is not None,
                "lint_score": original_scores["lint_score"]
            },
            "simplified": {
                "sentence": simplified,
                "valid": simplified_scores["lint_score"] is not None,
                "lint_score": simplified_scores["lint_score"]
            },
            "improvement": improvement,
            "generation_time": result["generation_time"],
            "alternatives_found": result["alternatives_found"]
        }

        return jsonify(response)

    except Exception as e:
        return jsonify(error="Processing failed", details=str(e)), 500

# Other
# ---------------------------------------------------------------

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5000
    print(f"✅ Server running on http://{host}:{port}")
    app.run(host=host, port=port, debug=False)

