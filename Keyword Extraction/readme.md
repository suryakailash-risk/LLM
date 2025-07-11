
# Keyword Extraction with Transformers

This project demonstrates how to extract **keyphrases** from a given text using a pre-trained **DistilBERT-based keyphrase extraction model** from [HuggingFace Transformers](https://huggingface.co/).

It uses the `ml6team/keyphrase-extraction-distilbert-inspec` model and the `pipeline` API to identify important keywords in a text.

---

## 🚀 Features

✅ Named Entity Recognition (NER) pipeline
✅ Uses `ml6team/keyphrase-extraction-distilbert-inspec` for keyphrase extraction
✅ Simple Python script with clear output
✅ Works with HuggingFace Transformers library

---

## 📦 Installation

1️⃣ Clone this repository (or save the script):

```bash
git clone <repo-url>
cd <repo-directory>
```

2️⃣ Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

3️⃣ Install the dependencies:

```bash
pip install transformers
```

---

## 📝 Usage

Run the script directly:

```bash
python Keyword Extraction.py
```

---

## 📄 Example Output

```bash
Extracted Keywords:
- Climate change
- pressing challenges
- 21st century
```

---

## 📚 References

* [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
* Model: [`ml6team/keyphrase-extraction-distilbert-inspec`](https://huggingface.co/ml6team/keyphrase-extraction-distilbert-inspec)

---

## 🧑‍💻 Author

Built by Suryakailash Ramesh.
