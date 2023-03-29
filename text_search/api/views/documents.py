from aiohttp_pydantic import PydanticView

import text_search.api.schema as schema


class SearchTextView(PydanticView):
    async def get(self, request: schema.DocumentSearchTextGetRequest):
        pass

class DeleteByIdView(PydanticView):
    async def delete(self, request: schema.DocumentDeleteRequest):
        pass