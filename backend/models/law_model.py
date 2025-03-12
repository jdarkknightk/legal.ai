from pydantic import BaseModel
from typing import List

class Law(BaseModel):
    category: str
    act: str
    section: str
    description: str
    keywords: List[str]
