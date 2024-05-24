from pyspark.sql import SparkSession

def correlate_data(impressions_path, clicks_path, conversions_path, output_path):
    spark = SparkSession.builder.appName("CorrelateData").getOrCreate()
    impressions = spark.read.parquet(impressions_path)
    clicks = spark.read.parquet(clicks_path)
    conversions = spark.read.parquet(conversions_path)

    clicks_conversions = clicks.join(conversions, on="user_id", how="inner")
    full_data = impressions.join(clicks_conversions, on="user_id", how="inner")
    full_data.write.parquet(output_path)

# Example usage
correlate_data('output/ad_impressions_transformed.parquet', 'output/clicks_transformed.parquet', 'output/conversions_transformed.parquet', 'output/full_data.parquet')

