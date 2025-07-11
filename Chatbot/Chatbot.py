from transformers import pipeline
chat_piprline = pipeline("text-generation", model="microsoft/DialoGPT-medium")
#memory for chat history
memory={}

def chat_with_memory( user_input):
    if "my name is" in user_input.lower():
        name = user_input.split("is")[-1].strip().split()[0]
        memory["name"] = name
        return f"Nice to meet you, {name}! How can I assist you today?"
    if 'name' in memory:
        user_input = f"Hello {memory['name']}, how can I help you?"
        respond = chat_piprline(user_input)
    else:
        respond = chat_piprline(user_input)
    return respond[0]['generated_text']

print("Chatbot is ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chat_with_memory(user_input)
    print(f"Chatbot: {response}")
