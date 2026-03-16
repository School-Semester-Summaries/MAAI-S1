import argparse
import json
import pandas as pd
from pathlib import Path
from lint_ii import ReadabilityAnalysis

parser = argparse.ArgumentParser()
parser.add_argument("--json", action="store_true")
args = parser.parse_args()

def calculate_readability(text: str) -> dict:
    try:
        analysis = ReadabilityAnalysis.from_text(text)
        return {"lint_score": analysis.lint.score}
    except:
        return {"lint_score": None}

def main():
    results_df = pd.read_parquet("results.parquet")
    row = results_df.iloc[0]

    original_scores = calculate_readability(row["original"])
    simplified_scores = calculate_readability(row["simplified"])

    result = {
        "original": {
            "sentence": row["original"],
            "valid": original_scores["lint_score"] is not None,
            "lint_score": original_scores["lint_score"]
        },
        "simplified": {
            "sentence": row["simplified"],
            "valid": simplified_scores["lint_score"] is not None,
            "lint_score": simplified_scores["lint_score"]
        },
        "improvement": None
    }

    if result["original"]["lint_score"] is not None and result["simplified"]["lint_score"] is not None:
        result["improvement"] = result["original"]["lint_score"] - result["simplified"]["lint_score"]

    # Save to temp.json
    with open("temp.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False)

if __name__ == "__main__":
    main()
