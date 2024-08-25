from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


templete = """
Answer the question below. If you don't know the answer.

Here is the convertation history {context}
Question: {question}
Answer : 
"""

model = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template(templete)
chain = prompt | model

def handel_conversation():
    context = ""
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input ("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": "user_input"})
        print("Bot: ", result)
        context+= f"\nUser:{user_input}\nAI: {result}"

if __name__ == "__main__":
    handel_conversation()





