
"""
This script checks sentences.csv and samples.csv for common data-entry
errors, such as:
  - a row with an empty required field
  - a duplicate sentence_id or sample_id
  - a sentence_id used in samples.csv that doesn't exist in sentences.csv
  - a split value that isn't train, val, or test

Usage (run from the repository root):
    python scripts/validate_dataset.py
"""

import csv


SENTENCES_FILE = "data/sentences.csv"
SAMPLES_FILE = "data/samples.csv"


errors = []


def read_csv(path):
    """Open a csv file and return its rows as a list of dicts."""
    with open(path, encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        return list(reader)


def normalize_id(value):
    """
    Prepare an id for comparison.
    Problem: some ids are written as "000290" and others as "290".
    These are different strings to a computer, even though they mean
    the same thing. If the id is purely numeric, this strips the
    leading zeros so "000290" and "290" both become "290" and can be
    compared safely.
    """
    value = value.strip()
    if value.isdigit():
        return str(int(value))
    return value


def check_sentences(rows):
    """
    Check sentences.csv.
    Returns the set of valid (normalized) sentence_ids, so we can
    later cross-check them against samples.csv.
    """
    already_seen = set()
    valid_ids = set()

    
    for row_number, row in enumerate(rows, start=2):
        sentence_id = row["sentence_id"].strip()
        text = row["text"].strip()

        if sentence_id == "":
            errors.append(f"sentences.csv row {row_number}: sentence_id is empty")
            continue  

        normalized = normalize_id(sentence_id)

        if normalized in already_seen:
            errors.append(f"sentences.csv row {row_number}: duplicate sentence_id -> {sentence_id}")

        already_seen.add(normalized)
        valid_ids.add(normalized)

        if text == "":
            errors.append(f"sentences.csv row {row_number}: text is empty")

    return valid_ids


def check_samples(rows, valid_sentence_ids):
    """Check samples.csv."""
    already_seen = set()
    allowed_splits = ["train", "val", "test"]

    for row_number, row in enumerate(rows, start=2):
        sample_id = row["sample_id"].strip()
        sentence_id = row["sentence_id"].strip()
        text = row["text"].strip()
        split = row["split"].strip()

        if sample_id == "":
            errors.append(f"samples.csv row {row_number}: sample_id is empty")
        elif sample_id in already_seen:
            errors.append(f"samples.csv row {row_number}: duplicate sample_id -> {sample_id}")
        already_seen.add(sample_id)

        if sentence_id == "":
            errors.append(f"samples.csv row {row_number}: sentence_id is empty")
        elif normalize_id(sentence_id) not in valid_sentence_ids:
            errors.append(f"samples.csv row {row_number}: sentence_id={sentence_id} not found in sentences.csv")

        if text == "":
            errors.append(f"samples.csv row {row_number}: text is empty")

        if split not in allowed_splits:
            errors.append(f"samples.csv row {row_number}: invalid split -> {split}")


def main():
    sentences_rows = read_csv(SENTENCES_FILE)
    samples_rows = read_csv(SAMPLES_FILE)

    valid_sentence_ids = check_sentences(sentences_rows)
    check_samples(samples_rows, valid_sentence_ids)

    print()
    if errors:
        print(f"{len(errors)} issue(s) found:")
        for error in errors:
            print(" -", error)
    else:
        print("Everything looks good, no issues found ✅")


if __name__ == "__main__":
    main()
