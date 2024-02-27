# data_dynamo_squad_project

This repository contains the code and configurations for a data engineering project aimed creating a data platform that extracts data from an operational database, archives it in a data lake, and makes it available in a remodelled OLAP data warehouse.

Key Features:
S3 Buckets
Two S3 buckets are used: one for ingested data and another for processed data.
Data is structured and immutable within these buckets.

Data Ingestion Application
A Python application continuously ingests tables from the totesys database into the "ingestion" S3 bucket.
The ingestion process is automatic, follows good security practices, with progress logged to Cloudwatch.
Email alerts are triggered in case of failures.

Data Processing Application
A Python application remodels data into a predefined schema suitable for a data warehouse.
Remodeled data is stored in Parquet format in the "processed" S3 bucket.
The application triggers automatically, is logged and monitored.
Populates dimension and fact tables of a single "star" schema in the warehouse.

Data Loading Application
A Python application loads data into a prepared data warehouse at defined intervals.
Adequately logged and monitored.

Testing and Compliance
All Python code is thoroughly tested, PEP8 compliant, and checked for security vulnerabilities.
Test coverage exceeds 90%.

Deployment
Infrastructure-as-code and CI/CD techniques are used for automatic deployment.
AWS services like AWS Eventbridge, S3 buckets, AWS Lambda, and Cloudwatch are utilized.

Data Sources
Primary data source: totesys database.

Tables to be ingested from the totesys database:
counterparty
currency
department
design
staff
sales_order
address
payment
purchase_order
payment_type
transaction

Tables to be populated in the warehouse are listed:
fact_sales_order
dim_staff
dim_location
dim_design
dim_date
dim_currency
dim_counterparty


Dashboard
A Quicksight dashboard is used to display warehouse data.
SQL queries for data retrieval are provided.


Technical Details
Hosted on AWS.
Utilizes AWS services such as AWS Eventbridge, S3 buckets, AWS Lambda, and Cloudwatch.
Logging and monitoring are managed through Cloudwatch, with email alerts for major errors.