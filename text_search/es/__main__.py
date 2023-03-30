import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from text_search.utils.config import AppConfig
from text_search.es.manager import EsManager
from text_search.es.mappings import documents_mapping


parser = ArgumentParser(
    formatter_class=ArgumentDefaultsHelpFormatter
)

group = parser.add_argument_group('Elasticsearch Options')
group.add_argument("--es-url", default=os.getenv('TEXT_SEARCH_ES_URL', AppConfig.es_url),
                   help="URL to use to connect to the Elasticsearch")
group.add_argument("--es-index", default=os.getenv('TEXT_SEARCH_ES_INDEX', AppConfig.es_index),
                   help="Index of the Elasticsearch to work with")

group = parser.add_argument_group('Commands')
group.add_argument("create", help="Create Elasticsearch index, which is set using the parameter --es-index")
group.add_argument("populate", help="Populate Elasticsearch index, which is set using the parameter --es-index, with data from csv file")


def main() -> None:
    args = parser.parse_args()

    es_manager = EsManager(args.es_url)
    if args.create is not None:
        es_manager.create_index(index=args.es_index, mapping=documents_mapping)
    elif args.populate is not None:
        es_manager.populate_index(index=args.es_index, path=args.populate)


if __name__ == '__main__':
    main()