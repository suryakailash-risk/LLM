Data="""LangChain is an open-source framework for developing applications powered by language models. 
It enables developers to build chatbots, agents, and tools that can interact with various data sources, 
perform reasoning, and maintain conversational context.

Core components of LangChain include:
- **LLM Wrappers**: Interfaces to large language models.
- **Chains**: Sequences of calls (to LLMs, APIs, etc.) to complete a task.
- **Agents**: Autonomous entities that decide what actions to take next.
- **Memory**: To maintain conversational or task context over time.
- **Document Loaders and Retrievers**: To load and search documents for relevant information.

LangChain can integrate with tools like Pinecone, Weaviate, FAISS for vector search, 
and supports frameworks like OpenAI GPT, HuggingFace Transformers, and more.

Use cases include:
- Question answering over documents
- Conversational agents
- Summarization
- Data extraction
"""
from transformers import pipeline
qa_pipeline = pipeline("question-answering",model="distilbert-base-uncased-distilled-squad",tokenizer="distilbert-base-uncased-distilled-squad")
question = "What is LangChain?"
qa_result = qa_pipeline(question=question, context=Data)
extracted_answer = qa_result['answer']
confidence = qa_result['score']
print(f"Question: {question}")
print(f"QA extracted answer: {extracted_answer} (confidence: {confidence:.2f})")
