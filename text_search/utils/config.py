from dataclasses import dataclass, field

from text_search.utils.argparse_u import positive_int


@dataclass
class AppConfig:
    address: str = field(default="0.0.0.0", 
                         metadata=dict(args=["--address"],
                         help="IPv4/IPv6 address API server would listen on"))

    port: positive_int = field(default=8080, 
                               metadata=dict(args=["--port"],
                               help="TCP port API server would listen on"))

    es_url: str = field(default="http://localhost:9200", 
                        metadata=dict(args=["--es-url"],
                        help="URL to use to connect to the Elasticsearch"))

    es_user: str = field(default="searcher", 
                         metadata=dict(args=["--es-user"],
                         help="Elasticsearch username"))

    es_pass: str = field(default="7Dx09Ns12Po6", 
                         metadata=dict(args=["--es-pass"],
                         help="Elasticsearch password"))

    es_index: str = field(default="text-search-index",
                          metadata=dict(args=["--es-index"],
                          help="Index of the Elasticsearch to work with"))

    db_url:  str = field(default="postgresql://searcher:3gkM5Rz79V@localhost/text_search_service", 
                         metadata=dict(args=["--db-url"],
                         help="URL to use to connect to the database"))
                         
    debug:   bool = field(default=False, metadata=dict(args=["--debug"]))