from typing import List
from elasticsearch import AsyncElasticsearch


class EsCrud:
    def __init__(self, es_url: str, es_user: str, es_pass: str, es_index: str):
        self.__es_client = AsyncElasticsearch(
            es_url,
            basic_auth=(es_user, es_pass)
        )
        self.es_index = es_index

    async def find_documents(self, text: str, limit: int = 20) -> List[int]:
        ids = list()
        
        try:
            resp = await self.__es_client.search(
                index=self.es_index,
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

        except Exception as e:
            return e
            

    async def del_document(self, id: int):
        try:
            await self.__es_client.delete_by_query(
                index=self.es_index,
                body={
                    "query": {
                        "match": {
                            "id": id
                        }
                    }
                }
            )

            return None

        except Exception as e:
            return e

    async def close(self):
        if self.__es_client is not None:
            try:
                await self.__es_client.close()
            except Exception as e:
                pass
            finally:
                self.__es_client = None