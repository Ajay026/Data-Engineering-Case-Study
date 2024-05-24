from pyspark.sql import SparkSession

def transform_data(input_path, output_path):
    spark = SparkSession.builder.appName("TransformData").getOrCreate()
    df = spark.read.json(input_path)
    df_transformed = df.withColumn("timestamp", df["timestamp"].cast("timestamp"))
    df_transformed.write.parquet(output_path)

# Example usage
transform_data('data/ad_impressions.json', 'output/ad_impressions_transformed.parquet')

