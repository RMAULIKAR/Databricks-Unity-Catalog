# Databricks notebook source
# MAGIC %md
# MAGIC ### Scenario - 1
# MAGIC **-Managed Catalog**
# MAGIC **-Managed Schema**
# MAGIC **-Managed Table**

# COMMAND ----------

# MAGIC %md
# MAGIC **Managed Catalog**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG man_cata

# COMMAND ----------

# MAGIC %md
# MAGIC **Managed Schema/Database**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA man_cata.man_schema

# COMMAND ----------

# MAGIC %md
# MAGIC **Managed Table**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE man_cata.man_schema.man_table
# MAGIC (
# MAGIC   id INT,
# MAGIC   name STRING
# MAGIC )
# MAGIC USING DELTA  

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO man_cata.man_schema.man_table
# MAGIC VALUES
# MAGIC (1,'ansh'),
# MAGIC (2,'lamba'),
# MAGIC (3,'TedX Speaker')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *FROM man_cata.man_schema.man_table
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scenario - 2
# MAGIC **-External Catalog**
# MAGIC **-Managed Schema**
# MAGIC **-Managed Table**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG ext_cata
# MAGIC MANAGED LOCATION 'abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/external_catalog'

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA ext_cata.man_schema

# COMMAND ----------

# MAGIC %sql
# MAGIC ----- Important created folder here ext_cata.man_schema.man_table2
# MAGIC CREATE TABLE ext_cata.man_schema.man_table2
# MAGIC (
# MAGIC   id INT,
# MAGIC   name STRING
# MAGIC )
# MAGIC USING DELTA  

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO ext_cata.man_schema.man_table2
# MAGIC VALUES
# MAGIC (1,'ansh'),
# MAGIC (2,'lamba'),
# MAGIC (3,'TedX Speaker')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *FROM ext_cata.man_schema.man_table2
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scenario - 3
# MAGIC **-External Catalog**
# MAGIC **-External Schema**
# MAGIC **-Managed Table**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA ext_cata.ext_schema
# MAGIC MANAGED LOCATION 'abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/external_catalog'

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE ext_cata.ext_schema.man_table3
# MAGIC (
# MAGIC   id INT,
# MAGIC   name STRING
# MAGIC )
# MAGIC USING DELTA  

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO ext_cata.ext_schema.man_table3
# MAGIC VALUES
# MAGIC (1,'ansh'),
# MAGIC (2,'lamba'),
# MAGIC (3,'TedX Speaker')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM ext_cata.ext_schema.man_table3

# COMMAND ----------

# MAGIC %md
# MAGIC ### Scenario - 4
# MAGIC **-External Table**

# COMMAND ----------

# MAGIC %sql
# MAGIC -- important -- stored at -- man_cata.man_schema.ext_table
# MAGIC CREATE TABLE man_cata.man_schema.ext_table
# MAGIC (
# MAGIC   id INT,
# MAGIC   name STRING
# MAGIC )
# MAGIC USING DELTA  
# MAGIC LOCATION 'abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/external_catalog/ext_table'

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO man_cata.man_schema.ext_table
# MAGIC VALUES
# MAGIC (1,'ansh'),
# MAGIC (2,'lamba'),
# MAGIC (3,'TedX Speaker')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM man_cata.man_schema.ext_table

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/external_catalog/ext_table` 
# MAGIC where id = 1

# COMMAND ----------

# MAGIC %sql
# MAGIC -- You have two ways to access the same external Delta table:
# MAGIC
# MAGIC -- Through Unity Catalog:
# MAGIC
# MAGIC SELECT *
# MAGIC FROM man_cata.man_schema.ext_table
# MAGIC WHERE id = 1;
# MAGIC
# MAGIC -- Directly through the Delta path:
# MAGIC
# MAGIC SELECT *
# MAGIC FROM delta.`abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/external_catalog/ext_table`
# MAGIC WHERE id = 1;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW EXTERNAL LOCATIONS;

# COMMAND ----------

# MAGIC %md
# MAGIC **DROP Managed Table**

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE man_cata.man_schema.man_table;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE ext_cata.man_schema.man_table2;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP CATALOG ext_cata;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP CATALOG ext_cata CASCADE;

# COMMAND ----------

# MAGIC %md
# MAGIC ### UNDROP Managed Table

# COMMAND ----------

# MAGIC %sql
# MAGIC UNDROP TABLE man_cata.man_schema.man_table;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Permanent Views

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VIEW man_cata.man_schema.view1
# MAGIC AS 
# MAGIC SELECT * FROM delta.`abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/external_catalog/ext_table`
# MAGIC WHERE id = 1 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM man_cata.man_schema.view1

# COMMAND ----------

# MAGIC %md
# MAGIC ### TEMP VIEWS

# COMMAND ----------

# MAGIC %md
# MAGIC **Temp View**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMP VIEW temp_view
# MAGIC AS 
# MAGIC SELECT * FROM delta.`abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/external_catalog/ext_table` 
# MAGIC WHERE id = 1 
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM temp_view

# COMMAND ----------

# MAGIC %md
# MAGIC ### VOLUMES

# COMMAND ----------

# MAGIC %md
# MAGIC **Creating a directory for volume**

# COMMAND ----------

dbutils.fs.mkdirs('abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/volumes')

# COMMAND ----------

# MAGIC %md
# MAGIC **Creating a volume**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE EXTERNAL VOLUME man_cata.man_schema.extvolume
# MAGIC LOCATION 'abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/volumes'

# COMMAND ----------

# MAGIC %md
# MAGIC **Copy file for volume**

# COMMAND ----------

dbutils.fs.cp('abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/source/sales', 'abfss://mycontainernew@storagefordatabricksrg.dfs.core.windows.net/volumes/sales', recurse=True)

# COMMAND ----------

# MAGIC %md
# MAGIC **Querying Volumes**

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM csv.`/Volumes/man_cata/man_schema/extvolume/sales`

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW EXTERNAL LOCATIONS;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE CATALOG EXTENDED man_cata;

# COMMAND ----------

# MAGIC %md
# MAGIC DELETE Catalog

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP CATALOG man_cata CASCADE;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP SCHEMA IF EXISTS man_cata.man_schema;

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DROP TABLE IF EXISTS man_cata.man_schema.man_table;