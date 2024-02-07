import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

database_name = "glue-lab"
table_name = "trusted"

dynamic_frame = glueContext.create_dynamic_frame.from_catalog(database=database_name, table_name=table_name)

selected_columns = dynamic_frame.select_fields(["original_title", "overview", "popularity", "release_date", "title", "vote_average", "vote_count"])

filtered_data = selected_columns.filter(
    lambda x: (x["title"] == "Get Out") | (x["title"] == "Us") | (x["title"] == "Nope")
)

spark_df = filtered_data.toDF()
spark_df = spark_df.coalesce(1)

spark_df.write.parquet("s3://bucketsprint8/Refined/Filmes/")