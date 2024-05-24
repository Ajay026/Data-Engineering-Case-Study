import csv
import boto3
from kafka import KafkaProducer

def ingest_csv_to_kafka(csv_file_path, kafka_topic):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    with open(csv_file_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            producer.send(kafka_topic, value=json.dumps(row).encode('utf-8'))
    producer.flush()

# Example usage
ingest_csv_to_kafka('data/clicks_conversions.csv', 'clicks-conversions-topic')

