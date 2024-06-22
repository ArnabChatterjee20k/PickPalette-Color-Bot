from langchain.pydantic_v1 import BaseModel,Field
from typing import List , Union
class PaletteParser(BaseModel):
    palette:Union[List[List[str]],List[str]] = Field(description="A list of palettes")