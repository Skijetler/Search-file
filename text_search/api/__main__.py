import os
from sys import argv
from argparse_dataclass import ArgumentParser
from setproctitle import setproctitle
import logging
from aiohttp import web

from text_search.utils.argparse_u import clear_environ
from text_search.utils.config import AppConfig
from text_search.api.app import create_app


# перфикс для переменных окружения
ENV_VAR_PREFIX = 'TEXT_SEARCH_'

# парсер параметров программы
parser = ArgumentParser(AppConfig,
                        auto_env_var_prefix=ENV_VAR_PREFIX)


def main() -> None:
    args = parser.parse_args()

    # выводит в списке процессов название программы
    setproctitle(os.path.basename(argv[0]))

    # очистка переменных окружения
    clear_environ(lambda i: i.startswith(ENV_VAR_PREFIX))

    app = create_app(args)
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    web.run_app(app, host=args.address, port=args.port)


if __name__ == '__main__': 
    main()