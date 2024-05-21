# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy jobs defined by deployment.yml

# COMMAND ----------

!pip install pyyaml

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Import libs

# COMMAND ----------

# Enable live reloading of libs, not needed now
# %load_ext autoreload
# %autoreload 2

# COMMAND ----------

import requests
from libs.dataops.deploy.autojob import autojob
from libs.dataops.job import run_job_by_name

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Create dev job

# COMMAND ----------

# Deploy jobs based on deployment.yml, in dev mode, specified by by env param
response = autojob(env="dev")

# COMMAND ----------

response

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Run job with python code

# COMMAND ----------

run_job_by_name(dbutils=dbutils, job_name=response['job_name'])

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Tasks for later
# MAGIC ### Task: Deploy to prod

# COMMAND ----------

# import os
# os.environ['PIPELINE_ENV'] = 'prod'
# # Deploy jobs based on deployment.yml, in dev mode
# prod_response = autojob(env="prod")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run prod job with python

# COMMAND ----------

# run_job_by_name(dbutils=dbutils, job_name=prod_response['job_name'])

# COMMAND ----------


