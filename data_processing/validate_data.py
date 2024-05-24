from pyspark.sql import SparkSession

def validate_data(input_path, output_path):
    spark = SparkSession.builder.appName("ValidateData").getOrCreate()
    df = spark.read.parquet(input_path)
    df_valid = df.dropDuplicates().na.drop()
    df_valid.write.parquet(output_path)

# Example usage
validate_data('output/full_data.parquet', 'output/full_data_valid.parquet')

