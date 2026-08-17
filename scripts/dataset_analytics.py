from pathlib import Path

import pandas as pd
import streamlit as st

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"

SENTENCES_FILE = DATA_DIR / "sentences.csv"
SAMPLES_FILE = DATA_DIR / "samples.csv"

st.set_page_config(
    page_title="DastKhat Dataset Analytics",
    layout="wide",
)

st.markdown(
    """
    <style>
        .metric-card {
            padding: 1rem;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.25);
            background-color: rgba(128, 128, 128, 0.05);
        }

        .coverage-container {
            margin-top: 10px;
            margin-bottom: 20px;
        }

        .coverage-bar {
            width: 100%;
            height: 18px;
            border-radius: 10px;
            background-color: #e5e7eb;
            overflow: hidden;
        }

        .coverage-fill {
            height: 100%;
            border-radius: 10px;
        }

        .rtl {
            direction: rtl;
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

@st.cache_data
def load_data():
    if not SENTENCES_FILE.exists():
        raise FileNotFoundError(
            f"Could not find sentences.csv at:\n{SENTENCES_FILE}"
        )

    if not SAMPLES_FILE.exists():
        raise FileNotFoundError(
            f"Could not find samples.csv at:\n{SAMPLES_FILE}"
        )

    sentences = pd.read_csv(
        SENTENCES_FILE,
        dtype={
            "sentence_id": str,
            "text": str,
        },
    )

    samples = pd.read_csv(
        SAMPLES_FILE,
        dtype={
            "sample_id": str,
            "participant_id": str,
            "sentence_id": str,
            "text": str,
            "split": str,
        },
    )

    sentences["sentence_id"] = (
        sentences["sentence_id"]
        .astype(str)
        .str.strip()
        .str.zfill(6)
    )

    samples["sentence_id"] = (
        samples["sentence_id"]
        .astype(str)
        .str.strip()
        .str.zfill(6)
    )

    return sentences, samples


def build_analytics(sentences, samples):
    sample_counts = (
        samples.groupby("sentence_id")
        .size()
        .rename("sample_count")
    )

    sentence_stats = sentences.copy()

    sentence_stats = sentence_stats.merge(
        sample_counts,
        how="left",
        left_on="sentence_id",
        right_index=True,
    )

    sentence_stats["sample_count"] = (
        sentence_stats["sample_count"]
        .fillna(0)
        .astype(int)
    )

    sentence_stats["has_sample"] = sentence_stats["sample_count"] > 0

    total_sentences = len(sentence_stats)

    covered_sentences = int(
        sentence_stats["has_sample"].sum()
    )

    uncovered_sentences = total_sentences - covered_sentences

    coverage_percentage = (
        covered_sentences / total_sentences * 100
        if total_sentences
        else 0
    )

    total_samples = len(samples)

    total_writers = (
        samples["participant_id"]
        .dropna()
        .nunique()
        if "participant_id" in samples.columns
        else 0
    )

    avg_samples_per_covered_sentence = (
        total_samples / covered_sentences
        if covered_sentences
        else 0
    )

    return {
        "sentence_stats": sentence_stats,
        "total_sentences": total_sentences,
        "covered_sentences": covered_sentences,
        "uncovered_sentences": uncovered_sentences,
        "coverage_percentage": coverage_percentage,
        "total_samples": total_samples,
        "total_writers": total_writers,
        "avg_samples_per_covered_sentence": avg_samples_per_covered_sentence,
    }


try:
    sentences, samples = load_data()

except Exception as e:
    st.error("Could not load the dataset.")
    st.exception(e)
    st.stop()


analytics = build_analytics(sentences, samples)

sentence_stats = analytics["sentence_stats"]

total_sentences = analytics["total_sentences"]
covered_sentences = analytics["covered_sentences"]
uncovered_sentences = analytics["uncovered_sentences"]
coverage_percentage = analytics["coverage_percentage"]
total_samples = analytics["total_samples"]
total_writers = analytics["total_writers"]
avg_samples = analytics["avg_samples_per_covered_sentence"]


st.title("DastKhat Dataset Analytics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Writers",
        f"{total_writers:,}",
    )

with col2:
    st.metric(
        "Total Samples",
        f"{total_samples:,}",
    )

with col3:
    st.metric(
        "Predefined Sentences",
        f"{total_sentences:,}",
    )

with col4:
    st.metric(
        "Sentence Coverage",
        f"{coverage_percentage:.2f}%",
    )




st.subheader("Sentence Coverage")

coverage_col1, coverage_col2, coverage_col3 = st.columns(3)

with coverage_col1:
    st.metric(
        "Sentences With Samples",
        f"{covered_sentences:,}",
    )

with coverage_col2:
    st.metric(
        "Sentences Without Samples",
        f"{uncovered_sentences:,}",
    )

with coverage_col3:
    st.metric(
        "Avg. Samples / Covered Sentence",
        f"{avg_samples:.2f}",
    )


st.markdown(
    f"""
    <div class="coverage-container">
        <div class="coverage-bar">
            <div
                class="coverage-fill"
                style="width: {coverage_percentage:.2f}%;
                       background-color: #22c55e;">
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


st.subheader("Samples per Sentence")

distribution = (
    sentence_stats["sample_count"]
    .value_counts()
    .sort_index()
)

distribution_df = distribution.reset_index()
distribution_df.columns = ["Samples per Sentence", "Number of Sentences"]

st.bar_chart(
    distribution_df.set_index("Samples per Sentence")
)


st.subheader("Coverage Breakdown")

bucket_0 = int(
    (sentence_stats["sample_count"] == 0).sum()
)

bucket_1 = int(
    (sentence_stats["sample_count"] == 1).sum()
)

bucket_2 = int(
    (sentence_stats["sample_count"] == 2).sum()
)

bucket_3_plus = int(
    (sentence_stats["sample_count"] >= 3).sum()
)

bucket_col1, bucket_col2, bucket_col3, bucket_col4 = st.columns(4)

with bucket_col1:
    st.metric(
        "0 Samples",
        f"{bucket_0:,}",
        help="Sentences that have never been submitted.",
    )

with bucket_col2:
    st.metric(
        "1 Sample",
        f"{bucket_1:,}",
    )

with bucket_col3:
    st.metric(
        "2 Samples",
        f"{bucket_2:,}",
    )

with bucket_col4:
    st.metric(
        "3+ Samples",
        f"{bucket_3_plus:,}",
    )



st.divider()

st.subheader("Sentences With No Samples")

uncovered_df = sentence_stats[
    sentence_stats["sample_count"] == 0
][
    ["sentence_id", "text"]
].copy()

uncovered_df.columns = [
    "Sentence ID",
    "Sentence",
]

st.metric(
    "Missing Sentences",
    f"{len(uncovered_df):,}",
)

if len(uncovered_df) > 0:

    search_missing = st.text_input(
        "Search uncovered sentences",
        placeholder="Type part of a Persian sentence...",
    )

    filtered_missing = uncovered_df.copy()

    if search_missing:
        filtered_missing = filtered_missing[
            filtered_missing["Sentence"]
            .str.contains(
                search_missing,
                case=False,
                na=False,
            )
        ]

    st.dataframe(
        filtered_missing,
        use_container_width=True,
        hide_index=True,
    )

    csv = filtered_missing.to_csv(
        index=False,
        encoding="utf-8-sig",
    )

    st.download_button(
        label="Download uncovered sentences",
        data=csv,
        file_name="uncovered_sentences.csv",
        mime="text/csv",
    )

else:
    st.success(
        "Every predefined sentence currently has at least one sample!"
    )


st.divider()

st.subheader("Sentence Explorer")

search_sentence = st.text_input(
    "Search sentences",
    placeholder="Search by sentence ID or Persian text...",
)

explorer_df = sentence_stats[
    [
        "sentence_id",
        "text",
        "sample_count",
    ]
].copy()

explorer_df.columns = [
    "Sentence ID",
    "Sentence",
    "Samples",
]

if search_sentence:

    mask = (
        explorer_df["Sentence ID"]
        .str.contains(
            search_sentence,
            case=False,
            na=False,
        )
        |
        explorer_df["Sentence"]
        .str.contains(
            search_sentence,
            case=False,
            na=False,
        )
    )

    explorer_df = explorer_df[mask]

st.dataframe(
    explorer_df,
    use_container_width=True,
    hide_index=True,
)


st.divider()

st.subheader("Dataset Integrity")

known_sentence_ids = set(
    sentences["sentence_id"]
)

unknown_sentence_samples = samples[
    ~samples["sentence_id"].isin(known_sentence_ids)
]

duplicate_sentence_ids = sentences[
    sentences["sentence_id"].duplicated(keep=False)
]

duplicate_sample_ids = samples[
    samples["sample_id"].duplicated(keep=False)
]


integrity_col1, integrity_col2, integrity_col3 = st.columns(3)

with integrity_col1:

    if len(unknown_sentence_samples) == 0:
        st.success("✓ All samples reference known sentences.")
    else:
        st.error(
            f"{len(unknown_sentence_samples):,} samples reference "
            "unknown sentence IDs."
        )

with integrity_col2:

    if len(duplicate_sentence_ids) == 0:
        st.success("✓ Sentence IDs are unique.")
    else:
        st.error(
            f"{len(duplicate_sentence_ids):,} duplicate sentence records."
        )

with integrity_col3:

    if len(duplicate_sample_ids) == 0:
        st.success("✓ Sample IDs are unique.")
    else:
        st.error(
            f"{len(duplicate_sample_ids):,} duplicate sample records."
        )


st.divider()

st.subheader("Dataset Summary")

summary_df = pd.DataFrame(
    {
        "Metric": [
            "Total writers",
            "Total handwritten samples",
            "Predefined sentences",
            "Sentences with ≥1 sample",
            "Sentences with 0 samples",
            "Sentence coverage",
            "Average samples per covered sentence",
        ],
        "Value": [
            f"{total_writers:,}",
            f"{total_samples:,}",
            f"{total_sentences:,}",
            f"{covered_sentences:,}",
            f"{uncovered_sentences:,}",
            f"{coverage_percentage:.2f}%",
            f"{avg_samples:.2f}",
        ],
    }
)

st.dataframe(
    summary_df,
    use_container_width=True,
    hide_index=True,
)
