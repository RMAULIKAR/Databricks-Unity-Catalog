# Databricks notebook source
# MAGIC %md
# MAGIC ### Delta Table

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE man_cata.man_schema.deltatbl
# MAGIC (
# MAGIC     id INT,
# MAGIC     name STRING,
# MAGIC     city STRING
# MAGIC )
# MAGIC USING DELTA
# MAGIC LOCATION 'abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net//deltalake/deltatbl'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE man_cata.man_schema.deltatbl
# MAGIC SET TBLPROPERTIES ('delta.enableDeletionVectors' = false);

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO man_cata.man_schema.deltatbl
# MAGIC VALUES
# MAGIC     (1, 'aa', 'delhi'),
# MAGIC     (2, 'bb', 'london'),
# MAGIC     (3, 'cc', 'sydney');

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE EXTENDED man_cata.man_schema.deltatbl;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM man_cata.man_schema.deltatbl;

# COMMAND ----------

# MAGIC %md
# MAGIC **UPDATE IN DELTA TABLE**

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC UPDATE man_cata.man_schema.deltatbl
# MAGIC SET city = 'toronto'
# MAGIC WHERE id = 1;

# COMMAND ----------

# MAGIC %md
# MAGIC **Versioning**

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY man_cata.man_schema.deltatbl;

# COMMAND ----------

# MAGIC %md
# MAGIC **Time Travel**

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC RESTORE man_cata.man_schema.deltatbl
# MAGIC TO VERSION AS OF 2;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM man_cata.man_schema.deltatbl;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE man_cata.man_schema.deltatbl
# MAGIC SET TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = false
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO man_cata.man_schema.deltatbl
# MAGIC VALUES
# MAGIC     (1, 'aa', 'delhi'),
# MAGIC     (2, 'bb', 'london'),
# MAGIC     (3, 'cc', 'sydney');

# COMMAND ----------

# MAGIC %md
# MAGIC ### Deletion Vector

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC ALTER TABLE man_cata.man_schema.deltatbl SET TBLPROPERTIES (
# MAGIC     'delta.enableDeletionVectors' = false
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE man_cata.man_schema.deltatbl2
# MAGIC (
# MAGIC     id INT,
# MAGIC     name STRING,
# MAGIC     city STRING
# MAGIC )
# MAGIC USING DELTA
# MAGIC LOCATION 'abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/deltalake/deltatbl2';

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO man_cata.man_schema.deltatbl2
# MAGIC VALUES
# MAGIC     (1, 'aa', 'delhi'),
# MAGIC     (2, 'bb', 'london'),
# MAGIC     (3, 'cc', 'sydney');

# COMMAND ----------

# MAGIC %md
# MAGIC **Updates in Deletion Vector Table**

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC UPDATE man_cata.man_schema.deltatbl2
# MAGIC SET city = 'seattle'
# MAGIC WHERE id = 1;

# COMMAND ----------

# MAGIC %md
# MAGIC ### OPTIMIZE IN DELTA TABLES

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY man_cata.man_schema.deltatbl2;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC OPTIMIZE man_cata.man_schema.deltatbl2;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Deep Clone vs Shallow Clone

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE man_cata.man_schema.deepclone_tbl
# MAGIC DEEP CLONE man_cata.man_schema.deltatbl;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE EXTENDED man_cata.man_schema.deepclone_tbl

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT *
# MAGIC FROM man_cata.man_schema.deepclonetbl;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT *
# MAGIC FROM man_cata.man_schema.deltatbl;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE HISTORY man_cata.man_schema.deepclonetbl;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE EXTENDED man_cata.man_schema.deepclonetbl;

# COMMAND ----------

# MAGIC %md
# MAGIC **Shallow Clone**

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE man_cata.man_schema.shallowtbl
# MAGIC SHALLOW CLONE man_cata.man_schema.man_table;

# COMMAND ----------

# MAGIC %sql DESCRIBE EXTENDED man_cata.man_schema.shallowtbl