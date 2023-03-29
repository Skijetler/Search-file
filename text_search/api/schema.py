from typing import List
from datetime import datetime
from pydantic import BaseModel, Extra


class Document(BaseModel):
    id: int
    rubrics: List[str]
    text: str
    created_date: datetime

class DocumentSearchTextGetRequest(BaseModel, extra=Extra.forbid):
    text: str

class DocumentSearchTextGetResponse(BaseModel):
    documents: List[Document]

class DocumentDeleteRequest(BaseModel, extra=Extra.forbid):
    id: int