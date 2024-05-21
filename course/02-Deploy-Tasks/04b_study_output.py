# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Study output
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Find the output data in Catalog page (from the left menu bar).
# MAGIC
# MAGIC What are the full Unity Catalog name of the output datasets? It will be under the catalog `acme_transport_taxinyc`.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC The upstream tables are:
# MAGIC
# MAGIC * acme_transport_taxinyc.dev_janisourander_featgh1019kajaani_bb599063_revenue.borough_population
# MAGIC * acme_transport_taxinyc.dev_janisourander_featgh1019kajaani_bb599063_revenue.revenue_by_borough
# MAGIC * training.taxinyc_trips.yellow_taxi_trips_curated_sample
# MAGIC
# MAGIC The downstream tables are:
# MAGIC
# MAGIC * acme_transport_taxinyc.dev_janisourander_featgh1019kajaani_bb599063_revenue.borough_population
# MAGIC * acme_transport_taxinyc.dev_janisourander_featgh1019kajaani_bb599063_revenue.revenue_by_borough
# MAGIC * acme_transport_taxinyc.dev_janisourander_featgh1019kajaani_bb599063_revenue.revenue_by_tripmonth
# MAGIC * acme_transport_taxinyc.dev_janisourander_featgh1019kajaani_bb599063_revenue.revenue_per_inhabitant

# COMMAND ----------


