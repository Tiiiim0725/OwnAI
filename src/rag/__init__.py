"""
RAG模块
提供文本分块、向量化和检索功能
"""
from rag.chunk import chunk_text, chunk_by_paragraph, chunk_by_sentence
from rag.embedding import EmbeddingClient, OpenAIEmbedding, init_embedding, encode_text
from rag.vector import VectorDB, init_vector_db, get_vector_db
from rag.rag import embedding, get_rag, init_rag, delete_collection, list_collections

__all__ = [
    # Chunk functions
    "chunk_text",
    "chunk_by_paragraph",
    "chunk_by_sentence",
    # Embedding
    "EmbeddingClient",
    "OpenAIEmbedding",
    "init_embedding",
    "encode_text",
    # Vector DB
    "VectorDB",
    "init_vector_db",
    "get_vector_db",
    # RAG main functions
    "embedding",
    "get_rag",
    "init_rag",
    "delete_collection",
    "list_collections",
]
