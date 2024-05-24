import json
import boto3
from kafka import KafkaProducer

def ingest_json_to_kafka(json_file_path, kafka_topic):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    with open(json_file_path) as f:
        for line in f:
            data = json.loads(line)
            producer.send(kafka_topic, value=json.dumps(data).encode('utf-8'))
    producer.flush()

# Example usage
ingest_json_to_kafka('data/ad_impressions.json', 'ad-impressions-topic')

