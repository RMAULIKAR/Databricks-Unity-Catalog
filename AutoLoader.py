# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %md
# MAGIC ### AUTOLOADER

# COMMAND ----------

# MAGIC %md
# MAGIC **Streaming Dataframe**

# COMMAND ----------

df = spark.readStream.format('cloudFiles') \
    .option('cloudFiles.format', 'parquet') \
    .option('cloudFiles.schemaLocation', 'abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/autosink/check') \
    .load('abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/autosource')

# COMMAND ----------

# Since df is a streaming DataFrame, you cannot use df.show() directly.
# To see the incoming data, use writeStream with the console sink

print(df)

# COMMAND ----------

# Yes — this error is because your current Databricks cluster/serverless compute does not support the continuous processingTime trigger.

# Your code:

# .trigger(processingTime='10 seconds')

# creates an infinite/continuous streaming query, which your current cluster type doesn't allow.


df.writeStream.format('parquet') \
    .option('checkpointLocation', 'abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/autosink/check') \
    .trigger(processingTime='10 seconds') \
    .start('abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/autosink/data')