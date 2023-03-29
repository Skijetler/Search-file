from dataclasses import dataclass, field


@dataclass
class AppConfig:
    address: str = field(default="0.0.0.0", 
                         metadata=dict(args=["--address"],
                         help="IPv4/IPv6 address API server would listen on"))

    port:    int = field(default=8080, 
                         metadata=dict(args=["--port"],
                         help="TCP port API server would listen on"))

    es_url:  str = field(default="http://localhost:9200", 
                         metadata=dict(args=["--es-url"],
                         help="URL to use to connect to the Elasticsearch"))
                         
    debug:   bool = field(default=False, metadata=dict(args=["--debug"]))