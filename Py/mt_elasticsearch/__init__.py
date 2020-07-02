from elasticsearch import Elasticsearch

ES_HOSTS = [
    {'host': 'hd1', 'port': 9200},
    {'host': 'hd3', 'port': 9200},
    {'host': 'hd9', 'port': 9200}
]
es = Elasticsearch(hosts=ES_HOSTS, request_timeout=6000, timeout=6000)


def update_by_query():
    """update_by_query"""
    print('''
q = {
    "source": "ctx._source.cname = params.name;ctx._source.cage = params.age;ctx._source.chome = params.home",
    "lang": "painless",
    "params": {
        "name": "wang",
        "age": "100",
        "home": "china"
    },
    "query": {
        "match": {
            "cid": "c2"
        }
    }
}
es.update_by_query(index="", body=q)
    ''')


def update_doc():
    """
    如果是修改特定
    id
    的文档，可以使用
    """
    print("""
POST twitter/doc/c2/_update
{
    "doc": {
        "cname": "wang",
        "cage": "100",
        "chome": "china"
    }
}
    """)

if __name__ == '__main__':
    pass