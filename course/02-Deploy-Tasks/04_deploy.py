# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy tasks
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Study: deployment.yml
# MAGIC
# MAGIC Look at `orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deployment.yml`.
# MAGIC It defines the job which will run the pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run dev deploy
# MAGIC
# MAGIC 1. Go to the notebook orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deploy
# MAGIC 2. connect to the UC Shared Cluster you have been assigned, and run through the cells
# MAGIC 3. Run the cells for deploying and running the dev job

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Look for the job under Workflows
# MAGIC
# MAGIC Workflows is on the side menu

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run the job by pressing the run button in the UI

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: What is the difference between a job and a job run?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Job is the defined task, a job run is a single instance of the defined task.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task: How was the job name composed?
# MAGIC
# MAGIC Write answer in the empty cell below.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC * DEV: 
# MAGIC     * acme_transport_taxinyc_prep_dev_janisourander_featgh1019kajaani_bb599063
# MAGIC * PRD: 
# MAGIC     * acme_transport_taxinyc_prep_prod_featgh1019kajaani_bb599063

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Where is the job cluster defined?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC In the YAML file: orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deployment.yml
# MAGIC
# MAGIC <br>
# MAGIC
# MAGIC ```yaml
# MAGIC tasks:
# MAGIC - task_key: revenue_by_borough
# MAGIC   run_if: ALL_SUCCESS
# MAGIC   existing_cluster_name: shared-job-cluster # <== HERE
# MAGIC ```
# MAGIC
# MAGIC It gets the dev/prod suffix later.
