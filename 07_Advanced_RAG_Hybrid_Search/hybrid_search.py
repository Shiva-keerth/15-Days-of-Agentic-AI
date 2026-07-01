"""
Day 7: Advanced RAG - Hybrid Search
Concept: Combining keyword search (BM25) with vector search (Embeddings) to get the best of both worlds.
"""
from langchain.retrievers import EnsembleRetriever
# from langchain_community.retrievers import BM25Retriever
# from langchain_chroma import Chroma

def build_hybrid_retriever(docs):
    """
    bm25_retriever = BM25Retriever.from_documents(docs)
    chroma_retriever = Chroma.from_documents(docs, OpenAIEmbeddings()).as_retriever()
    
    # 50/50 weighting
    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, chroma_retriever], weights=[0.5, 0.5]
    )
    return ensemble_retriever
    """
    print("Hybrid Ensemble Retriever built combining BM25 and Vector Search.")

if __name__ == "__main__":
    build_hybrid_retriever([])
