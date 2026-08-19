# Azure Databricks & Unity Catalog

A hands-on practice repository created to build practical understanding of **Azure Databricks, Delta Lake, Databricks Workflows, Unity Catalog, and modern data management concepts**.

The repository focuses on understanding how Databricks features work in practice rather than only learning their theoretical concepts.

## 📚 Topics Covered

* **Databricks Workflows** for notebook orchestration
* **Delta Lake** and the structure of Delta tables
* Understanding the **Delta transaction log**
* Practical exploration of Delta operations and table history
* **Metastore and Unity Catalog**
* Managed and external catalogs/tables
* Schemas and tables
* Data and object lifecycle when objects are deleted
* **Temporary and permanent views**
* **Volumes** and file management in Unity Catalog
* **Auto Loader** for incremental file ingestion

---

## 📓 Practice Notebooks

| Notebook            | Purpose                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Notebook1.py`      | Demonstrates Databricks **Workflow** concepts and notebook orchestration                                                                                             |
| `Notebook2.py`      | Additional hands-on practice with **Databricks Workflows**                                                                                                           |
| `delta_tutorial.py` | Practical exploration of **Delta Lake**, including Delta table structure, transaction logs, operations, and understanding what happens internally when data changes  |
| `tutorial_1.py`     | Hands-on exploration of **Unity Catalog and data governance concepts**, including Metastore, catalogs, managed/external objects, schemas, tables, views, and volumes |
| `AutoLoader.py`     | Practice with **Auto Loader** and incremental file ingestion                                                                                                         |

---

## 🔹 Delta Lake Practice

The `delta_tutorial.py` notebook focuses on building a practical understanding of **Delta Lake**.

Rather than only creating Delta tables, the notebook explores what happens behind the scenes, including:

* Delta table structure
* Transaction log
* Delta table versions
* Data files and transaction history
* Insert, update, and delete operations
* How changes are recorded in the Delta log
* Understanding table history and versioning

The objective is to understand **how Delta Lake works internally and how to interpret the changes recorded in the transaction log**.

---

## 🔹 Unity Catalog Practice

The `tutorial_1.py` notebook focuses on understanding **Unity Catalog and Databricks data organization** through hands-on experimentation.

Topics include:

* Metastore
* Unity Catalog
* Catalogs
* Managed and external catalogs/tables
* Schemas
* Tables
* Object and data lifecycle
* What happens when data or catalog objects are deleted
* Temporary views
* Permanent views
* Volumes

The focus is on understanding the relationship between these objects and how Databricks manages data and metadata.

---

## 🔹 Databricks Workflows

`Notebook1.py` and `Notebook2.py` are used to demonstrate **Databricks Workflow concepts**, including running notebooks as part of an orchestrated workflow.

The purpose is to gain practical exposure to how multiple notebook tasks can be organized and executed through Databricks Workflows.

---

## 🔹 Auto Loader

`AutoLoader.py` provides hands-on practice with **Databricks Auto Loader** for incremental file ingestion.

The notebook focuses on understanding how new files can be detected and processed as they arrive rather than repeatedly processing the complete source directory.

---

## 🎯 Objective

The purpose of this repository is to demonstrate practical understanding of key **Azure Databricks data engineering concepts** through hands-on experimentation, with particular focus on:

**Databricks Workflows · Delta Lake · Transaction Logs · Auto Loader · Unity Catalog · Metastore · Catalogs · Schemas · Tables · Views · Volumes**
