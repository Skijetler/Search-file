from aiohttp.web import Application
from aiohttp_pydantic import oas

from text_search.api.views import documents
from text_search.es.crud import EsCrud
from text_search.utils.config import AppConfig


def create_app(config: AppConfig) -> Application:

    app = Application()
    app["es"] = EsCrud(es_url=config.es_url, es_index=config.es_index)
    if config.debug_mode:
        oas.setup(app, url_prefix='/swagger')

    app.router.add_view("/docs/search", documents.SearchTextView)
    app.router.add_view("/docs/delete", documents.DeleteByIdView)


    return app