import uuid
from pydantic import BaseModel, ConfigDict, Field
from src.utils.logging import logger
"""
这里的chunk还需要考虑从sql中、md文本、json中读取信息以及直接接收大模型调用的情况。
"""
class Chunk(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True,
        extra="allow",
    )
    info_type: str = Field(description="The type of the chunk")
    data_source: str = Field(description="The path to the source file of the chunk")
    data_description: str = Field(description="The description content of the chunk")
    data_dict: dict = Field(description="The full data record as a dictionary")
    datetime: int = Field(description="The datetime when the chunk was created")
    metadata: dict = Field(
        default_factory=dict,
        description="The metadata of the chunk",
    )

    @property
    def chunk_id(self) -> str:
        content_str = f"{self.info_type}_{self.data_source}_{self.data_description}"
        return str(uuid.uuid5(uuid.NAMESPACE_DNS, content_str))
    
    def to_qdrant_payload(self) -> dict:
        return {
            "data_description": self.data_description,
            "info_type": self.info_type,
            "data_source": self.data_source,
            "data_dict": self.data_dict,
            "datetime": self.datetime,
            **self.metadata,
        }

class Processor:
    def __init__(self):
        pass

    def process(
        self, 
        info_type: str, 
        data_source: str, 
        data_description: str, 
        data_dict: dict, 
        datetime: int, 
        metadata: dict = None
    ) -> Chunk | None:
        pass
