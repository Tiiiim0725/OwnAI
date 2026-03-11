from abc import ABC, abstractmethod
from src.rag.chunk import Chunk

from src.utils.logging import logger

class IVectorStore(ABC):
    @abstractmethod
    def add(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        pass

    @abstractmethod
    def search(self, query: list[float], top_k: int, table_name: str | None = None, score_threshold: float | None = None) -> list[dict]:
        pass

    @abstractmethod
    def get_all_points(self) -> list[dict]:
        pass

class QdrantVectorStore(IVectorStore):
    def __init__(
        self,
        url: str,
        api_key: str,
        collection_name: str,
        prefer_grpc: bool = True,
        dimension: int = 3072,
    ):
        from qdrant_client import QdrantClient
        self.client = QdrantClient(url, api_key, collection_name, prefer_grpc)
        self.dimension = dimension
        pass