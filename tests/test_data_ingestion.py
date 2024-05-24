import pytest
from data_ingestion.json_ingestion import ingest_json_to_kafka

def test_ingest_json_to_kafka(mocker):
    mocker.patch('kafka.KafkaProducer.send')
    ingest_json_to_kafka('data/ad_impressions.json', 'test-topic')
    assert True  # Add more assertions based on Kafka producer mocks

