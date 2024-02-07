import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)


input_path = "s3://bucketsprint8/Raw/TMDB/JSON/2023/09/30/tmdb_movies_2017_2020.json"


output_path = "s3://bucketsprint8/Trusted/Filmes2017-2020/"


df = spark.read.json(input_path)

df.write.parquet(output_path, mode="overwrite")

job.commit()