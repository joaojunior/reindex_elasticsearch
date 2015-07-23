import argparse

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def reindex_elasticsearch(index_from, index_to, hosts_from, hosts_to=[], type_from=None,  type_to=None, bulk_size = 10, number_of_shards=1, number_of_replicas=0):
    es = Elasticsearch(hosts=hosts_from)
    es.indices.create(index=index_to, ignore=400, body = {'number_of_shards' : number_of_shards, 'number_of_replicas': number_of_replicas})
    if hosts_to:
        es_to = Elasticsearch(hosts=hosts_to)
    else:
        es_to = es
    query = {"from" : 0, "size" : bulk_size, "query": { "match_all": {}}}
    result = es.search(index = index_from, doc_type = type_from, body  = query)
    total_docs = result['hits']['total']
    number_pages = calculate_number_pages(total_docs, bulk_size)
    change_index_and_type_doc(result['hits']['hits'], index_to, type_to)
    bulk(client=es_to, actions=result['hits']['hits'], chunk_size=bulk_size)
    for i in xrange(1, number_pages):
        query['from'] = i * bulk_size
        result = es.search(index = index_from, doc_type = type_from, body  = query)
        change_index_and_type_doc(result['hits']['hits'], index_to, type_to)
        bulk(client=es_to, actions=result['hits']['hits'], chunk_size=bulk_size)

def calculate_number_pages(total_docs, docs_by_page):
    number_pages = total_docs / docs_by_page
    if total_docs % docs_by_page != 0:
        number_pages += 1
    return number_pages

def change_index_and_type_doc(docs, index, type=None):
    for doc in docs:
        doc["_index"] = index
        if type:
            doc["_type"] = type

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("index_from", help="Index Source", type=str)
    parser.add_argument("index_to", help="Index Dest", type=str)
    parser.add_argument("host_from", help="Ip Host from", type=str)
    parser.add_argument("type_from", help="Type doc from", type=str)
    parser.add_argument("type_to", help="Type doc to", type=str)
    parser.add_argument("--host_to", help="Ip Host to. Default is same host_from", type=str)
    parser.add_argument("--bulk_size", help="Size of Bulk. Default is 10.", default=10, type=int)
    parser.add_argument("--number_of_shards", help="Shards to new index. Default is 1.", default=1, type=int)
    parser.add_argument("--number_of_replicas", help="Replicas to new index. Default is 0.", default=0, type=int)
    args = parser.parse_args()
    if args.hosts_to:
        host_to = [args.host_to]
    else:
        host_to = [args.host_from]
    reindex_elasticsearch(args.index_from, args.index_to, [args.host_from], host_to, 
        args.type_from,  args.type_to, args.bulk_size, args.number_of_shards, args.number_of_replicas)