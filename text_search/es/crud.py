from typing import List
from elasticsearch import AsyncElasticsearch


class EsCrud:
    def __init__(self, es_url: str, es_index: str):
        self.__es_client = AsyncElasticsearch(es_url)
        self.__es_index = es_index

    async def find_documents(self, text: str, limit: int = 20) -> List[int]:
        ids = list()
        resp = await self.__es_client.search(
            index=self.__es_index,
            body={
                "query": {
                    "match": {
                        "text": text
                    }
                }
            },
            size=limit
        )

        for doc in resp["hits"]["hits"]:
            ids.append(doc["_source"]["id"])

        return ids