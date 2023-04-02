import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, BooleanOptionalAction

from text_search.utils.config import AppConfig
from text_search.es.manager import EsManager
from text_search.es.mappings import documents_mapping


parser = ArgumentParser(
    formatter_class=ArgumentDefaultsHelpFormatter
)

group = parser.add_argument_group("Elasticsearch Options")
group.add_argument("--es-url", default=os.getenv("TEXT_SEARCH_ES_URL", AppConfig.es_url),
                   help="Elasticsearch URL [env var: TEXT_SEARCH_ES_URL]")
group.add_argument("--es-user", default=os.getenv("TEXT_SEARCH_ES_USER", AppConfig.es_user),
                   help="Elasticsearch username [env var: TEXT_SEARCH_ES_USER]")
group.add_argument("--es-pass", default=os.getenv("TEXT_SEARCH_ES_PASS", AppConfig.es_pass),
                   help="Elasticsearch password [env var: TEXT_SEARCH_ES_PASS]")
group.add_argument("--es-index", default=os.getenv("TEXT_SEARCH_ES_INDEX", AppConfig.es_index),
                   help="Index of the Elasticsearch [env var: TEXT_SEARCH_ES_INDEX]")

group = parser.add_argument_group("Commands")
group.add_argument("--create", default=False, action=BooleanOptionalAction,
                    help="Create Elasticsearch index, which is set using the parameter --es-index")
group.add_argument("--populate", default="",
                    help="Populate Elasticsearch index, which is set using the parameter --es-index, with data from csv file")


def main() -> None:
    args = parser.parse_args()

    es_manager = EsManager(es_url=args.es_url, es_user=args.es_user, es_pass=args.es_pass)
    if args.create:
        es_manager.create_index(index_name=args.es_index, mapping=documents_mapping)
    elif args.populate != "":
        es_manager.populate_index(index_name=args.es_index, path=args.populate)


if __name__ == '__main__':
    main()