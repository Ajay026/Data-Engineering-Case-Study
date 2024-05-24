import pytest
from data_storage.setup_storage import setup_storage

def test_setup_storage(spark):
    data_path = 'tests/output/full_data_valid.parquet'
    table_name = 'test_full_data'
    setup_storage(data_path, table_name)
    df = spark.sql(f"SELECT * FROM {table_name}")
    assert df.count() > 0  # Add more validations based on expected storage setup
