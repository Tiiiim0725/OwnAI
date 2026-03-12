from src.rag.chunk import Chunk, Processor
from src.rag.embedding import EmbeddingModel
from src.rag.vector import QdrantVectorStore



class RAGSystem:
    def __init__(
        self, 
        qdrant_url: str,
        qdrant_api_key: str,
        qdrant_collection_name: str,
        embedding_url: str,
        embedding_api_key: str,
        embedding_model: str,
    ):
        self.vector_store = QdrantVectorStore(
            url=qdrant_url,
            api_key=qdrant_api_key,
            collection_name=qdrant_collection_name,
        )
        self.embedding_url = embedding_url
        self.embedding_api_key = embedding_api_key
        self.embedding_model = embedding_model

        self.embedding_model = EmbeddingModel(
            url=self.embedding_url,
            api_key=self.embedding_api_key,
            model=self.embedding_model,
        )

    def search(
        self,
        query: str,
        k: int = 5, # RAG检索返回数据数量，后期我们需要研究这个默认值设置多少合适
        score_threshold: float | None = 0.5,
    ) -> list[dict]:
        embeddings = self.embedding_model.embed_batch([query])[0]
        results = self.vector_store.search(
            embeddings, k, score_threshold
        )
        return results

    def build_context(
        self,
        query: str,
        k: int = 5, # RAG检索返回数据数量，后期我们需要研究这个默认值设置多少合适
        score_threshold: float | None = 0.5,
    ) -> str:
        results = self.search(query, k, score_threshold)

        if not results:
            return None
        else:
            return results

    def embed(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        result = self.embedding_model.embed_batch(texts)
        return result

    def chunk(
        self,
        query: str,
        k: int = 5, # RAG检索返回数据数量，后期我们需要研究这个默认值设置多少合适
        score_threshold: float | None = 0.5,
    ) -> list[dict]:
        pass

    def upsert(
        self,
        chunks: list[Chunk],
        batch_size: int = 100,
    ) -> None:
        self.vector_store.upsert(chunks, batch_size=batch_size)
        return None # 这个函数还需要后续更新功能。