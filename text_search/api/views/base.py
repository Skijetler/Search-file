from functools import partial
import ujson
from aiohttp import web
from aiohttp_pydantic import PydanticView


UJSONResponse = partial(web.json_response, dumps=ujson.dumps)


class BaseView(PydanticView):

    @property
    def es_crud(self):
        return self.request.app["es_crud"]

    @property
    def db_session(self):
        return self.request.app["db_session"]