# 🤖 Conversational Chatbot with Transformers

This project implements a simple **conversational chatbot** using the HuggingFace [Transformers](https://huggingface.co/docs/transformers) library and the pre-trained model **microsoft/DialoGPT-medium**.

The chatbot can hold a back-and-forth conversation with a user using natural language.

---

## 🚀 Features

* Uses `microsoft/DialoGPT-medium` (a medium-sized DialoGPT model fine-tuned for dialogues).
* Supports multi-turn conversations via the `Conversation` class.
* Simple and easy-to-run Python script.
* Based on HuggingFace `transformers` and `pipeline`.

---

## 📦 Installation

1️⃣ Clone this repository (or save the script):

```bash
git clone https://github.com/suryakailash-risk/LLM.git
cd Chatbot
```

2️⃣ (Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3️⃣ Install dependencies:

```bash
pip install transformers
```

---

## 📝 Usage

Run the chatbot:

```bash
python chatbot.py
```

### Example Code (`chatbot.py`):

```python
from transformers import pipeline, Conversation

# Load the conversational pipeline
chat_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")

# Start a conversation
conversation = Conversation("Hello, how are you?")
response = chat_pipeline(conversation)

# Print the bot's response
print(response)
```

---

## 💬 Example Output

```bash
>> User: Hello, how are you?
Bot: I'm good! How can I help you today?
```

---

## 🧰 Troubleshooting

🔹 If you see:

```
KeyError: "Unknown task conversational"
```

It means your `transformers` version is outdated.
➡️ Upgrade it:

```bash
pip install --upgrade transformers
```
```bash
pip install --upgrade streamlit
```

---

## 📚 References

* [Transformers Documentation](https://huggingface.co/docs/transformers/index)
* [microsoft/DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium)

---

## 🧑‍💻 Author

By suryakailash