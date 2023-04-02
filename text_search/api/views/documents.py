from aiohttp_pydantic.oas.typing import r200, r410

from text_search.api.views.base import BaseView, UJSONResponse
import text_search.api.schema as schema
import text_search.db.crud as crud


class SearchTextView(BaseView):
    async def get(self, request: schema.DocumentSearchTextGetRequest) -> r200[schema.DocumentSearchTextGetResponse]:
        """
        Find documents by text
        
        Tags: docs
        Status Codes:
            200: Documents found
        """
        resp = schema.DocumentSearchTextGetResponse(documents=[])
        documents_ids = await self.es_crud.find_documents(request.text)
        if isinstance(documents_ids, Exception) or not documents_ids:
            return UJSONResponse(data=resp.dict(), status=404)
        db_documents = await crud.get_documents(db=self.db_session, document_ids=documents_ids)
        for db_document in db_documents:
            resp.documents.append(schema.Document(
                id=db_document.id,
                rubrics=db_document.rubrics,
                text=db_document.text,
                created_date=schema.JsonDatetime(
                    year=db_document.created_date.year,
                    month=db_document.created_date.month,
                    day=db_document.created_date.day,
                    hour=db_document.created_date.hour,
                    minute=db_document.created_date.minute,
                    second=db_document.created_date.second
                )
            ))
        resp.documents.sort(key=lambda doc: doc.created_date)
        return UJSONResponse(data=resp.dict())

class DeleteByIdView(BaseView):
    async def delete(self, request: schema.DocumentDeleteRequest) -> r410:
        """
        Delete document by id

        Tags: docs
        Status Codes:
            410: Document deleted
        """
        return UJSONResponse(status=410)