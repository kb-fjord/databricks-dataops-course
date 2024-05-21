# Databricks notebook source
# MAGIC %md
# MAGIC ## Create the revenue data product
# MAGIC #

# COMMAND ----------

# %load_ext autoreload
# %autoreload 2

# COMMAND ----------

from libs.dataops.job.params import job_param

# COMMAND ----------

# Import pyspark utility functions
from pyspark.sql import functions as F

# Name functions enables automatic env+user specific database naming
from libs.tblname import tblname
from libs.catname import catname_from_path
from libs.dbname import dbname

# COMMAND ----------

# git_commit = job_param(dbutils=dbutils, param="git_commit")
# print("git_commit: " + repr(git_commit))

# COMMAND ----------

cat = catname_from_path()
db = dbname(db="revenue", cat=cat)
print("New db name: " + db)
spark.sql(f"USE catalog {cat}")
spark.sql(f"CREATE DATABASE IF NOT EXISTS {db}")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Get input dataset
# MAGIC ...and show a few records of input dataset

# COMMAND ----------

trips_df = spark.sql(
    "select * from training.taxinyc_trips.yellow_taxi_trips_curated_sample"
)
trips_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Revenue sum by pickup_borough
# MAGIC
# MAGIC `total_amount` is the revenue for a trip.
# MAGIC
# MAGIC Sort by pickup_borough ascending.

# COMMAND ----------

revenue_by_borough_df = (
    trips_df.groupBy("pickup_borough")
    .agg(F.sum("total_amount").alias("amount"))
    .sort(F.col("pickup_borough").asc())
)
revenue_by_borough_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Write dataset

# COMMAND ----------

catalog = catname_from_path()
print(f"catalog: {catalog}")

# COMMAND ----------

revenue_by_borough_df

# COMMAND ----------

revenue_by_borough_tbl = tblname(cat=catalog, db="revenue", tbl="revenue_by_borough")
print("revenue_by_borough_tbl:" + repr(revenue_by_borough_tbl))
(
    revenue_by_borough_df.write.mode("overwrite")
    .format("delta")
    .saveAsTable(revenue_by_borough_tbl)
)

# COMMAND ----------


