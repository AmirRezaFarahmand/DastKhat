# DastKhat

## Persian Handwritten Text Dataset

**DastKhat** (دستخط, meaning *handwriting*) is an open Persian handwritten text dataset created for research and development in **Optical Character Recognition (OCR)**, **Handwritten Text Recognition (HTR)**, and related machine learning tasks.

The dataset consists of handwritten Persian sentences collected from multiple participants. Each participant wrote a set of predefined Persian sentences, allowing the dataset to capture variation in handwriting styles, letter shapes, spacing, and writing patterns.

> **This repository does not contain an AI model.**
> It is the GitHub repository for the dataset project, its metadata, processing tools, and documentation.

---

## Dataset

The handwritten images are hosted on Hugging Face:

### 🤗 DastKhat Dataset

**https://huggingface.co/datasets/MrFarahmand/DastKhat**

The Hugging Face dataset contains the actual handwritten image samples.

The GitHub repository intentionally does **not** contain the image files. This keeps the code repository lightweight and makes the dataset easier to distribute through a platform designed for large datasets.

---

## Repository Structure

```text
DastKhat/
│
├── dataset/
│   └── samples.csv
│
├── scripts/
│   ├── ...
│   └── ...
│
├── CONTRIBUTORS.md
├── README.md
└── LICENSE
```

The exact structure may evolve as the dataset and processing pipeline develop.

---

## Dataset Metadata

The dataset metadata describes each handwritten sample.

### `samples.csv`

The sample metadata contains the following fields:

| Column           | Description                                             |
| ---------------- | ------------------------------------------------------- |
| `sample_id`      | Unique identifier for the handwritten sample            |
| `participant_id` | Identifier of the person who wrote the sample           |
| `image_path`     | Path or reference to the corresponding image            |
| `sentence_id`    | Identifier of the sentence                              |
| `text`           | Ground-truth Persian transcription                      |
| `split`          | Dataset split, such as training, validation, or testing |

The image files corresponding to these samples are available through the Hugging Face dataset.

---

## Example Record

```csv
sample_id,participant_id,image_path,sentence_id,text,split
000001,participant_001,participant_001/000001.png,000001,متن نمونه فارسی,train
```

The actual dataset contains handwritten Persian samples collected from multiple participants.

---

## Loading the Dataset

You can load the dataset using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("MrFarahmand/DastKhat")
```

Inspect the dataset:

```python
print(dataset)
```

Access a sample:

```python
sample = dataset["train"][0]

print(sample)
```

Depending on the dataset configuration, the image can be accessed from the `image` field:

```python
image = sample["image"]
text = sample["text"]

print(text)
image.show()
```

---

## Dataset Design

DastKhat is designed around **writer diversity**.

Different participants naturally produce different:

* Letter shapes
* Writing styles
* Character connections
* Word spacing
* Writing sizes
* Slants and angles
* Pen pressure patterns
* Individual handwriting characteristics

This makes the dataset useful for studying the challenges involved in recognizing real Persian handwriting.

---

## Potential Applications

DastKhat can be used for research and experimentation in areas such as:

* Persian Handwritten Text Recognition (HTR)
* Persian Optical Character Recognition (OCR)
* Deep Learning
* Computer Vision
* Document Image Analysis
* Writer Identification
* Handwriting Style Analysis
* Data Augmentation
* Self-Supervised Learning
* Sequence Recognition

The dataset is intended to provide a foundation for building and evaluating future Persian handwriting recognition systems.

---

## Data Collection

The dataset was created by collecting handwritten samples from multiple participants.

Each participant was provided with predefined Persian sentences and asked to write them by hand. The handwritten submissions were then processed and converted into individual image samples with corresponding metadata.

The processing pipeline includes steps such as:

1. Collecting handwritten submissions
2. Extracting handwritten regions
3. Cropping individual samples
4. Associating samples with their ground-truth text
5. Organizing metadata
6. Preparing the dataset for machine learning applications

---

## GitHub and Hugging Face

The project is intentionally divided between two platforms:

### GitHub

Used for:

* Dataset documentation
* Metadata
* Processing scripts
* Data preparation tools
* Project development

### Hugging Face

Used for:

* Hosting the handwritten image data
* Dataset distribution
* Loading the dataset for machine learning workflows

👉 **Download and access the dataset on Hugging Face:**

https://huggingface.co/datasets/MrFarahmand/DastKhat

---

## Loading the Dataset

The dataset can be downloaded using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("MrFarahmand/DastKhat")
```

The exact dataset structure and available splits can be inspected with:

```python
print(dataset)
```

---

## Project Status

🚧 **Active Development**

The dataset is still being expanded and improved.

Future improvements may include:

* More participants
* More handwriting samples
* Improved metadata
* Additional dataset splits
* Improved preprocessing
* More detailed documentation
* Benchmark models and baseline experiments

---

## Contributing

Contributions are welcome.

Possible ways to contribute include:

* Contributing Persian handwritten samples
* Improving data processing scripts
* Finding and fixing dataset issues
* Improving documentation
* Developing preprocessing tools
* Creating baseline experiments
* Reporting problems with the dataset

If you would like to contribute handwritten data, please open an issue or contact the project maintainer.

---

## Citation

If you use DastKhat in your research or project, please cite the dataset.

A formal citation will be added as the dataset reaches a more stable release.

---

## License

Please see the repository license for information about using, modifying, and redistributing the project and dataset.

---

## Author

Created and maintained by **Amir Reza Farahmand**.

* GitHub: [AmirRezaFarahmand](https://github.com/AmirRezaFarahmand)
* Hugging Face: [MrFarahmand](https://huggingface.co/MrFarahmand)

---

## Acknowledgements

Special thanks to all participants who contributed their handwritten Persian samples to the creation of this dataset.

Without their contributions, DastKhat would not exist.
