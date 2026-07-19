# DastNevis

**DastNevis** is an open dataset initiative for **Persian handwritten text recognition (HTR)**. The project aims to collect diverse handwritten Persian samples from contributors and build a high-quality dataset for research and development in OCR, HTR, and computer vision.

## 🎯 Goals

* Build a diverse dataset of handwritten Persian text.
* Collect handwriting samples from people with different writing styles.
* Provide structured metadata for each handwritten sample.
* Support research and experimentation in Persian Handwritten Text Recognition.
* Make Persian handwriting data more accessible to the machine learning community.

## 📊 Dataset

The dataset consists of handwritten Persian sentences collected from multiple contributors.

Each sample is associated with its original text and relevant metadata, allowing researchers to connect handwritten images with their corresponding transcriptions.

The dataset is currently under active development.

## 🗂️ Dataset Structure

The repository is organized to separate the dataset components:

```text
DastNevis/
├── data/
│   ├── images/
│   └── metadata/
├── docs/
├── scripts/
├── LICENSE
└── README.md
```

The exact structure may evolve as the dataset grows.

## 🧾 Metadata

Each handwritten sample is linked to a unique sentence identifier.

Example:

```csv
sentence_id,text
000001,این یک نمونه جمله فارسی است.
000002,یادگیری ماشین یکی از شاخه‌های هوش مصنوعی است.
```

The metadata allows each handwritten image to be matched with its ground-truth transcription.

## ✍️ Data Collection

DastNevis uses a contributor-based data collection process. Contributors are provided with Persian sentences and write them by hand.

This approach allows the dataset to capture natural variation in:

* Handwriting styles
* Letter shapes
* Word spacing
* Writing speed
* Pen and paper characteristics
* Individual writing habits

This diversity is essential for developing models that can generalize beyond a single person's handwriting.

## 🤖 Intended Applications

The dataset is intended for research and experimentation in areas such as:

* Persian Handwritten Text Recognition
* Optical Character Recognition (OCR)
* Computer Vision
* Deep Learning
* Document Analysis
* Persian Language Technology

## 🚧 Project Status

**Early Development**

DastNevis is currently in the data collection and dataset development phase. The dataset will continue to grow as more handwritten samples are collected and validated.

## 🤝 Contributing

Contributions are welcome.

You can help by:

* Contributing handwritten samples
* Improving data collection tools
* Developing preprocessing and validation scripts
* Improving documentation
* Building baseline HTR models
* Reporting issues and suggesting improvements

## 📜 License

The dataset license will be specified as the project develops.

## 🌱 Vision

The long-term goal of DastNevis is to create an open, diverse, and high-quality resource for Persian handwritten text recognition and help advance research in Persian language AI.

**Every handwritten sentence contributes to teaching machines how humans write Persian.**
