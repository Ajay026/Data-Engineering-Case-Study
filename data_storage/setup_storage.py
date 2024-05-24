from pyspark.sql import SparkSession

def setup_storage(data_path, table_name):
    spark = SparkSession.builder.appName("SetupStorage").enableHiveSupport().getOrCreate()
    df = spark.read.parquet(data_path)
    df.write.saveAsTable(table_name)

# Example usage
setup_storage('output/full_data_valid.parquet', 'advertisex.full_data')

