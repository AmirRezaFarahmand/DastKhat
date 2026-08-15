from pathlib import Path
import pandas as pd
import json

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / Path("data")

samples = pd.read_csv(DATA_DIR / "samples.csv")
sentences = pd.read_csv(DATA_DIR / "sentences.csv")

writers_count = samples["participant_id"].nunique()
samples_count = len(samples)
sentences_count = len(sentences)

stats = {
    "writers": int(writers_count),
    "samples": int(samples_count),
    "sentences": int(sentences_count),
}

DOCS_DIR = ROOT_DIR / Path("docs")
BADGES_DIR = DOCS_DIR / Path("badges")
BADGES_DIR.mkdir(parents=True, exist_ok=True)

def create_badge(label: str, message: str, color: str):
    return {
        "schemaVersion": 1,
        "label": label,
        "message": message,
        "color": color,
    }

badges = {
    "writers.json": create_badge(
        " ",
        f"{writers_count:,}",
        "blue",
    ),
    "samples.json": create_badge(
        " ",
        f"{samples_count:,}",
        "green",
    ),
    "sentences.json": create_badge(
        " ",
        f"{sentences_count:,}",
        "orange",
    ),
}

for filename, content in badges.items():
    with open(BADGES_DIR / filename, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2)