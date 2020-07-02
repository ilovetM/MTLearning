def reindex():
    print('''
POST /_reindex
{
  "source": {
    "index": "test_dmr_new",
    "query": {
      "term": {
        "type": "peak"
      }
    }
  },
  "dest": {
    "index": "test_peak"
  }
}
''')


def create_index_with_setting():
    print('''
PUT /test.peak_reference
{
  "settings": {
    "index" : {
        "number_of_shards": 10,
        "number_of_replicas" : 0
    }
  }
}
    ''')


def put_index_replicas():
    print('''
PUT test_dmr_new/_settings
{
  "index": {
    "number_of_replicas" : 1
  }
}
''')


if __name__ == '__main__':
    reindex()
    create_index_with_setting()
    put_index_replicas()
