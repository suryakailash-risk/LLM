

# 🦎 Qameleon — Question Answering with Transformers

This project demonstrates how to use the 🤗 **Transformers** library to build a simple Question Answering (QA) pipeline powered by a pretrained **DistilBERT** model fine-tuned on SQuAD.

It asks a question about a text context (here: *What is LangChain?*), extracts an answer, and reports the confidence.

---

## 📄 Example Output

```
Question: What is LangChain?
QA extracted answer: LangChain is an open-source framework for developing applications powered by language models (confidence: 0.87)
```

---

## 🚀 How It Works

✅ Loads a **question-answering pipeline** from Hugging Face 🤗
✅ Provides a text *context* and a *question*
✅ The LLM extracts the most relevant answer span from the context
✅ Reports the answer and the model's confidence score

---

## 🧰 Requirements

* Python ≥ 3.7
* `transformers` library

Install dependencies:

```bash
pip install transformers
```

---

## 📚 References

* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
* [DistilBERT: smaller, faster, cheaper](https://arxiv.org/abs/1910.01108)

---

## ✨ Author

Surya Kailash Ramesh

### 🏃‍♀️ 4️⃣ Run the script

Run your Python file from the terminal:

```bash
python text_questions.py
```

