import os
from pathlib import Path
from langchain_text_splitters import MarkdownHeaderTextSplitter

def load_markdown_files(markdown_dir: str) -> dict[str, str]:
    markdown_files = {}
    
    for file_path in Path(markdown_dir).glob("*.md"):
        with open(file_path, "r", encoding="utf-8") as f:
            markdown_files[file_path.name] = f.read()
    
    return markdown_files

def split_markdown_documents(markdown_text: str, source_file: str = "") -> list[dict]:
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    splits = splitter.split_text(markdown_text)
    
    documents = []
    for split in splits:
        # Get header values
        h1 = split.metadata.get("Header 1", "")
        h2 = split.metadata.get("Header 2", "")
        h3 = split.metadata.get("Header 3", "")
        
        # Build section path ("Schrijfstijl > Schrijf begrijpelijk > Bijvoorbeeld")
        section_parts = [h for h in [h1, h2, h3] if h]
        section_path = " > ".join(section_parts)
        
        # Reconstruct the full text with complete header hierarchy
        header_parts = []
        if h1:
            header_parts.append(f"# {h1}")
        if h2:
            header_parts.append(f"## {h2}")
        if h3:
            header_parts.append(f"### {h3}")
        
        # Combine headers with content for full context
        full_text = "\n".join(header_parts) + "\n" + split.page_content if header_parts else split.page_content
        
        doc = {
            "text": full_text,
            "source": source_file or "",
            "section_path": section_path,
        }
        
        documents.append(doc)
    
    return documents

def process_all_markdown_files(markdown_dir: str) -> list[dict]:
    all_documents = []
    
    markdown_files = load_markdown_files(markdown_dir)
    
    for filename, content in markdown_files.items():
        
        # Remove the filepath comment if present
        lines = content.split("\n")
        
        if lines and lines[0].startswith("// filepath:"):
            content = "\n".join(lines[1:])
        
        documents = split_markdown_documents(content, source_file=filename)
        all_documents.extend(documents)
        
    return all_documents