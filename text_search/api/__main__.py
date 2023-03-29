import os
from argparse_dataclass import ArgumentParser
from aiohttp import web

from text_search.utils.config import AppConfig
from text_search.api.app import create_app


# парсер параметров программы
parser = ArgumentParser(AppConfig)


def main():
    args = parser.parse_args()

    app = create_app(args)
    web.run_app(app, host=args.address, port=args.port)

if __name__ == '__main__': 
    main()