import pytest
from data_processing.transform_data import transform_data

def test_transform_data(spark):
    input_path = 'tests/data/ad_impressions.json'
    output_path = 'tests/output/ad_impressions_transformed.parquet'
    transform_data(input_path, output_path)
    df = spark.read.parquet(output_path)
    assert df.count() > 0  # Add more validations based on expected transformations
