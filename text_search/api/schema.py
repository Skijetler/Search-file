from typing import List
from datetime import datetime
from pydantic import BaseModel, Extra


class JsonDatetime(datetime):
    def __json__(self):
        return '"%s"' % self.strftime("%Y-%m-%d %H:%M:%S")


class Document(BaseModel):
    id: int
    rubrics: List[str]
    text: str
    created_date: JsonDatetime

class DocumentSearchTextGetRequest(BaseModel, extra=Extra.forbid):
    text: str

class DocumentSearchTextGetResponse(BaseModel):
    documents: List[Document]

class DocumentDeleteRequest(BaseModel, extra=Extra.forbid):
    id: int