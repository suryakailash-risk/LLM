# 📄 Document Summarizer with BART

This project demonstrates how to summarize long documents using the **Hugging Face Transformers** library and the **facebook/bart-large-cnn** model.

## 🚀 Features

✅ Summarizes text into concise paragraphs
✅ Uses `pipeline` from 🤗 Transformers
✅ Adjustable summary length parameters

---

## 🛠️ Requirements

Make sure you have **Python 3.7+** and install the following library:

```bash
pip install transformers
```

---

## 📋 How to Run

1️⃣ Save the script as `summarizer.py`.

2️⃣ Run the script in your terminal:

```bash
python summarizer.py
```

3️⃣ Output:
The script prints a summarized version of the input text to the console.

---

## 📝 Example

Input text:

> Climate change is one of the most pressing challenges of the 21st century, affecting ecosystems, economies, and communities worldwide...

Output summary:

> Climate change threatens ecosystems, economies, and communities through extreme weather. Reducing emissions via renewable energy, efficiency, and forest protection is vital, supported by global cooperation.

---

## 📚 Notes

* The model used is `facebook/bart-large-cnn`, which is fine-tuned for summarization.
* You can adjust `max_length`, `min_length`, and `do_sample` in the function to control the summary.
* Internet connection is required the first time to download the model.

---

---
## ✨ Author

Surya Kailash Ramesh
## 📚 References

---