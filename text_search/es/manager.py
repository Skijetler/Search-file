import json
import logging
from typing import Dict
from elasticsearch import Elasticsearch
import pandas as pd
import numpy as np


logging.basicConfig(level=logging.INFO)


class EsManager:
    def __init__(self, es_url):
        self.__es_client = Elasticsearch(es_url)
        logging.info(self.__es_client.ping())

    def create_index(self, index_name: str, mapping: Dict) -> None:
        """
        Create an ES index.
        :param index_name: Name of the index.
        :param mapping: Mapping of the index
        """
        logging.info("Creating index {index_name} with the following schema:\n{schema}".format(index_name=index_name, schema=json.dumps(mapping, indent=2)))
        self.__es_client.indices.create(index=index_name, ignore=400, body=mapping)

    def populate_index(self, path: str, index_name: str) -> None:
        """
        Populate an index from a CSV file.
        :param path: The path to the CSV file.
        :param index_name: Name of the index to which documents should be written.
        """
        df = pd.read_csv(path).replace({np.nan: None})
        logging.info("Writing {indexes_count} documents to ES index {index_name}".format(indexes_count=len(df.index), index_name=index_name))
        for doc in df.apply(lambda x: x.to_dict(), axis=1):
            self.__es_client.index(index=index_name, body=json.dumps(doc))