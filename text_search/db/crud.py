from sqlalchemy.orm import Session
from typing import List

import text_search.db.models as models


async def get_document(db: Session, document_id: int):
    return db.query(models.Document).filter(models.Document.id == document_id).first()

async def get_documents(db: Session, document_ids: List[int]):
    return db.query(models.Document).filter(models.Document.id.in_(document_ids)).all()

async def del_document(db: Session, document_id: int):
    db_document = await get_document(db, document_id)
    db.delete(db_document)
    db.commit()