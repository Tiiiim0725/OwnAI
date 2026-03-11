from abc import ABC, abstractmethod
from enum import Enum
from dotenv import load_dotenv
from src.utils.logging import logger
load_dotenv()

class IEmbeddingModel(ABC):
    @abstractmethod
    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        pass

class EmbeddingModel(IEmbeddingModel):
    def __init__(self, model: IEmbeddingModel):
        self.model = model
    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        pass