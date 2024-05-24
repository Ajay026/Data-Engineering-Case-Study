import avro.schema
import avro.io
import io
from kafka import KafkaProducer

def ingest_avro_to_kafka(avro_file_path, kafka_topic, schema_path):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    schema = avro.schema.parse(open(schema_path, "r").read())
    
    with open(avro_file_path, 'rb') as f:
        reader = DataFileReader(f, DatumReader())
        for record in reader:
            bytes_writer = io.BytesIO()
            encoder = avro.io.BinaryEncoder(bytes_writer)
            datum_writer = avro.io.DatumWriter(schema)
            datum_writer.write(record, encoder)
            raw_bytes = bytes_writer.getvalue()
            producer.send(kafka_topic, value=raw_bytes)
    producer.flush()

# Example usage
ingest_avro_to_kafka('data/bid_requests.avro', 'bid-requests-topic', 'schemas/bid_request.avsc')

