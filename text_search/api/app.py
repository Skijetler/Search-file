from functools import partial

from aiohttp.web import Application
from aiohttp_pydantic import oas

from text_search.api.views import documents
from text_search.utils.db import db_session, es_crud
from text_search.utils.config import AppConfig


def create_app(config: AppConfig) -> Application:

    app = Application()

    # Подключение на старте к индексу ES и отключение при остановке
    app.cleanup_ctx.append(partial(
        es_crud, 
        es_url=config.es_url, 
        es_user=config.es_user, 
        es_pass=config.es_pass, 
        es_index=config.es_index
    ))
    
    # Подключение на старте к базе данных и отключение при остановке
    app.cleanup_ctx.append(partial(db_session, db_url=config.db_url))

    if config.debug:
        # Swagger документация
        oas.setup(app, url_prefix='/swagger', title_spec="Text Search")

    app.router.add_view("/docs/search", documents.SearchTextView)
    app.router.add_view("/docs/delete", documents.DeleteByIdView)


    return app