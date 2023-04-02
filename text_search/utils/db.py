import os
from typing import Union
from types import SimpleNamespace
from pathlib import Path
from configargparse import Namespace

from aiohttp.web import Application
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from text_search.es.crud import EsCrud


PROJECT_PATH = Path(__file__).parent.parent.resolve()

def make_alembic_config(cmd_opts: Union[Namespace, SimpleNamespace],
                        base_path: str = PROJECT_PATH) -> Config:
    """
    Создает объект конфигурации alembic на основе аргументов командной строки,
    подменяет относительные пути на абсолютные.
    """
    # Подменяем путь до файла alembic.ini на абсолютный
    if not os.path.isabs(cmd_opts.config):
        cmd_opts.config = os.path.join(base_path, cmd_opts.config)

    config = Config(file_=cmd_opts.config, ini_section=cmd_opts.name,
                    cmd_opts=cmd_opts)

    # Подменяем путь до папки с alembic на абсолютный
    alembic_location = config.get_main_option('script_location')
    if not os.path.isabs(alembic_location):
        config.set_main_option('script_location',
                               os.path.join(base_path, alembic_location))
    if cmd_opts.db_url:
        config.set_main_option('sqlalchemy.url', cmd_opts.db_url)

    return config

async def db_session(app: Application, db_url: str):
    engine = create_engine(url=db_url, connect_args={"options": "-c timezone=utc"})
    app["db_session"] = Session(engine)
    yield
    app["db_session"].close()
    app["db_session"].get_bind().dispose()

async def es_crud(app: Application, es_url: str, es_user: str, es_pass: str, es_index: str):
    app["es_crud"] = EsCrud(es_url=es_url, es_user=es_user, es_pass=es_pass, es_index=es_index)
    yield
    await app["es_crud"].close()