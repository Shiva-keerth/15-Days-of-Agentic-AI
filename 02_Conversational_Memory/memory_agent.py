"""
Day 2: Conversational Memory Agent
Concept: Adding memory to an agent so it remembers the history of the conversation, allowing for follow-up questions.
"""
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain

def chat_with_memory():
    llm = ChatOpenAI(temperature=0.7)
    # Remember the last 5 interactions
    memory = ConversationBufferWindowMemory(k=5)
    
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    
    print(conversation.predict(input="Hi, my name is Shiva."))
    print(conversation.predict(input="What is my name?"))

if __name__ == "__main__":
    chat_with_memory()
