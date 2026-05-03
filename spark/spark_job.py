"""PySpark job for lab 2.

Reads a small in-memory dataset, calculates basic statistics,
and prints a summary to the Spark executor logs.
"""

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max as spark_max, min as spark_min, sum as spark_sum

conf = SparkConf().setAppName("Lab2 PySpark Job").setMaster("spark://spark-master:7077")

spark = SparkSession.builder.config(conf=conf).getOrCreate()
spark.sparkContext.setLogLevel("WARN")

data = [(1, "alice", 42), (2, "bob", 17), (3, "carol", 35), (4, "dave", 28), (5, "eve", 51)]
columns = ["id", "name", "value"]

df = spark.createDataFrame(data, columns)
df.show()

stats = df.select(
    spark_sum("value").alias("total"),
    avg("value").alias("mean"),
    spark_min("value").alias("min"),
    spark_max("value").alias("max"),
)
stats.show()

print("Lab 2 Spark job completed successfully.")

spark.stop()
