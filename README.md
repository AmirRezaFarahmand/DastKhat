# DastKhat (دستخط)

[![License](https://img.shields.io/github/license/AmirRezaFarahmand/DastKhat)](LICENSE)
[![Hugging Face Dataset](https://img.shields.io/badge/HuggingFace-Dataset-yellow?logo=huggingface)](https://huggingface.co/datasets/MrFarahmand/DastKhat)
[![GitHub stars](https://img.shields.io/github/stars/AmirRezaFarahmand/DastKhat?style=social)](https://github.com/AmirRezaFarahmand/DastKhat)


## Persian Handwritten Text Dataset

DastKhat is an open-source Persian handwritten text dataset created for **Optical Character Recognition (OCR)** and **Handwritten Text Recognition (HTR)** research.

The project focuses on collecting, processing, and publishing sentence-level handwritten Persian data to help researchers and developers build better Persian handwriting recognition systems.

The dataset contains handwritten Persian sentences collected from multiple contributors with different writing styles. Each handwritten sample is linked to its original Persian text annotation and metadata.

The dataset is publicly available on Hugging Face:

https://huggingface.co/datasets/MrFarahmand/DastKhat

---

# Project Goals

Persian handwriting recognition remains a challenging problem due to:

- Limited publicly available Persian handwriting datasets
- Large variation in handwriting styles
- Complex Persian character forms and cursive writing
- Lack of diverse writer-independent datasets

DastKhat aims to provide an accessible resource for:

- Persian OCR research
- Handwritten Text Recognition models
- Computer Vision experiments
- Document understanding systems
- Academic projects and competitions

---

# Dataset Overview

| Metric | Value |
|---|---:|
| Writers | 8 |
| Unique Sentences | 700 |
| Handwritten Samples | 560 |
| Language | Persian (فارسی) |
| Annotation Level | Sentence |
| Image Format | RGB |
| License | MIT |
| Current Version | v0.1 |

---

# Repository Structure

```
DastKhat/

├── data/
│   ├── samples.csv
│   └── sentences.csv
│
├── docs/
│   └── Project documentation
│
├── scripts/
│   └── Data collection and processing tools
│
├── CONTRIBUTORS.md
├── LICENSE
└── README.md
```

---

# Dataset Metadata

The dataset metadata is stored inside the `data/` directory.

## `sentences.csv`

Contains the predefined Persian sentences used during data collection.

| Field | Description |
|---|---|
| `sentence_id` | Unique identifier of the sentence |
| `text` | Persian sentence content |

Example:

```csv
sentence_id,text
000001,امروز هوا بسیار خوب است.
000002,یادگیری ماشین یکی از شاخه‌های هوش مصنوعی است.
```

---

## `samples.csv`

Contains information about each handwritten sample.

| Field | Description |
|---|---|
| `sample_id` | Unique identifier for handwritten sample |
| `participant_id` | Identifier of contributor |
| `sentence_id` | Related sentence identifier |
| `text` | Ground truth transcription |
| `split` | Dataset split |

Example:

```csv
sample_id,participant_id,sentence_id,text,split
000001,P001,000001,امروز هوا بسیار خوب است.,train
```

---

# Data Collection Pipeline

The dataset is created through the following workflow:

```
Sentence Generation
        |
        v
Handwriting Sheet Creation
        |
        v
Participant Writing
        |
        v
Scanning / Image Collection
        |
        v
Handwritten Region Detection
        |
        v
Sentence Image Cropping
        |
        v
Metadata Generation
        |
        v
Dataset Release
```

---

# Contributing

DastKhat is an open-source project and contributions are welcome.

There are several ways to contribute:

## Handwriting Contribution

Participants can contribute handwritten Persian samples through:

https://www.alacrity.ir

Contributors will be acknowledged in future dataset releases and publications.

---

## Code Contribution

Developers can contribute by:

- Improving preprocessing scripts
- Adding data validation tools
- Improving documentation
- Creating visualization tools
- Developing training pipelines
- Reporting bugs and suggesting improvements

Before contributing, please read:

```
CONTRIBUTORS.md
```

---

# Development Setup

Clone the repository:

```bash
git clone https://github.com/AmirRezaFarahmand/DastKhat.git

cd DastKhat
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

*(Dependency setup will be added as the processing pipeline evolves.)*

---

# Data Processing Scripts

The `scripts/` directory contains utilities used for:

- Dataset generation
- Image preprocessing
- Metadata creation
- Validation
- Dataset maintenance

Each script contains its own documentation and usage instructions.

---

# Usage

DastKhat can be used for:

- Persian OCR systems
- Handwritten text recognition models
- CNN/Transformer-based vision models
- Document AI research
- Writer identification experiments
- Handwriting style analysis

Recommended evaluation metrics:

- Character Error Rate (CER)
- Word Error Rate (WER)
- Sequence Accuracy

---

# Dataset Versions

## v0.1

Initial public release.

Included:

- 8 writers
- 560 handwritten samples
- 700 predefined sentences

---

## Future Plans

Planned improvements:

- Increase number of contributors
- Expand handwriting styles
- Improve dataset validation
- Add more benchmark experiments
- Release training baselines

---

# Citation

If you use DastKhat in your research, please cite:

```bibtex
@dataset{farahmandfar2026dastkhat,
  author = {Farahmandfar, AmirReza},
  title = {DastKhat: A Persian Handwritten Text Dataset},
  year = {2026},
  publisher = {Hugging Face},
  url = {https://huggingface.co/datasets/MrFarahmand/DastKhat}
}
```

---

# License

This project is released under the MIT License.

See:

```
LICENSE
```

for more information.

---

# Acknowledgements

Special thanks to everyone who contributed their handwriting samples and helped make DastKhat possible.

---

# Maintainer

**AmirReza Farahmand**

- GitHub: https://github.com/AmirRezaFarahmand
- Hugging Face: https://huggingface.co/MrFarahmand