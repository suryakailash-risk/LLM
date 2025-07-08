# 🎭 EmotiCheck — What’s Your Text Feeling?

**EmotiCheck** is a simple and interactive sentiment analysis tool powered by 🤗 Transformers.
It analyzes the sentiment of any text you enter and tells you whether it’s **Positive** or **Negative**, along with a confidence score.

---

## 🚀 Features

✅ Real-time sentiment analysis of user-provided text
✅ Uses the powerful `distilbert-base-uncased-finetuned-sst-2-english` model
✅ Runs entirely locally in Python
✅ Interactive CLI — keeps running until you exit

---

## 📝 Example Output

```
Enter text for sentiment analysis (or type 'exit' to quit): I love programming!
Sentiment: POSITIVE, Score: 0.99

Enter text for sentiment analysis (or type 'exit' to quit): This is frustrating.
Sentiment: NEGATIVE, Score: 0.97

Enter text for sentiment analysis (or type 'exit' to quit): exit
Exiting sentiment analysis.
```

---

## 🧰 Requirements

* Python ≥ 3.7
* HuggingFace Transformers library

Install dependencies:

```bash
pip install transformers
```

---

## 🔧 How to Run

1️⃣ Save the file called:

```text
Sentiment_Analysis.py
```

2️⃣ Run the script from your terminal:

```bash
python Sentiment_Analysis.py
```

3️⃣ Type your text when prompted and see the sentiment result.
Type `exit` to quit the program.

---
## ✨ Author

Surya Kailash Ramesh
## 📚 References

---

* [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
* [DistilBERT SST-2 Model](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english)

