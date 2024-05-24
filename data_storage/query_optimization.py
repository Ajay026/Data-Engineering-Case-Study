from pyspark.sql import SparkSession

def optimize_query():
    spark = SparkSession.builder.appName("QueryOptimization").enableHiveSupport().getOrCreate()
    spark.sql("SET hive.execution.engine=tez")
    spark.sql("SET hive.exec.dynamic.partition=true")
    spark.sql("SET hive.exec.dynamic.partition.mode=nonstrict")
    spark.sql("SET hive.optimize.ppd=true")

# Example usage
optimize_query()

