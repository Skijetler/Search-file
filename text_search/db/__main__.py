"""
Утилита для управления состоянием базы данных, обертка над alembic.
Можно вызывать из любой директории, а также указать произвольный DSN для базы
данных, отличный от указанного в файле alembic.ini.
"""
import argparse
import logging
import os

from alembic.config import CommandLine

from text_search.utils.db import make_alembic_config
from text_search.utils.config import AppConfig


def main():
    logging.basicConfig(level=logging.DEBUG)

    alembic = CommandLine()
    alembic.parser.formatter_class = argparse.ArgumentDefaultsHelpFormatter
    alembic.parser.add_argument(
        "--db-url", default=os.getenv("TEXT_SEARCH_DB_URL", AppConfig.db_url),
        help="Database URL [env var: TEXT_SEARCH_DB_URL]"
    )

    options = alembic.parser.parse_args()
    if 'cmd' not in options:
        alembic.parser.error("too few arguments")
    else:
        config = make_alembic_config(options)
        exit(alembic.run_cmd(config, options))


if __name__ == '__main__':
    main()
