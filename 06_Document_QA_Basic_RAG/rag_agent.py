"""
Day 6: Document Q&A Agent (Basic RAG)
Concept: Retrieval-Augmented Generation. Loading a document, chunking it, storing it in ChromaDB, and querying it.
"""
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def run_basic_rag():
    # 1. Load & Chunk
    # loader = TextLoader("knowledge.txt")
    # docs = loader.load()
    # 2. Embed & Store
    # vectorstore = Chroma.from_documents(docs, OpenAIEmbeddings())
    # 3. Retrieve & Generate
    print("Basic RAG pipeline initialized. Ready to process chunks.")

if __name__ == "__main__":
    run_basic_rag()
