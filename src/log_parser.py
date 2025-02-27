from elasticsearch import Elasticsearch
import pandas as pd

# Connect to Elasticsearch in Kubernetes Kind Cluster
es = Elasticsearch(["http://elasticsearch-master.default.svc.cluster.local:9200"])

def fetch_logs(index="logstash-*"):
    query = {"size": 1000, "query": {"match_all": {}}}
    res = es.search(index=index, body=query)

    logs = [{"timestamp": hit["_source"]["@timestamp"], "message": hit["_source"]["message"]} for hit in res["hits"]["hits"]]
    return pd.DataFrame(logs) if logs else pd.DataFrame()
