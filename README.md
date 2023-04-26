# End To End Fred API Data Pipeline
## Table of contents
* [Problem Statement](#problem-statement)
* [Technologies](#technologies)
* [Project Data flow](#project-data-flow)
* [Reproducability](#reproducability)
* [Further Improvements](#further-improvements)
## Problem Statement
This project implement concept learn from [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) course. 
To build a pipeline to ingest the data store them in a datalake and process them into Data warehouse.

The Data used in this project is from [FRED Economic Data](https://fred.stlouisfed.org/docs/api/fred). Using the FRED API to call the data using Python with Prefect Orchestration.
Store them into Google Cloud Storage Bucket and Using DBT to transform data into the BigQuery and connect with Looker Studio to find insigh from the data. 

There are multiple data in FRED Economic data. I want to create a pipeline to ingest these data base on the topic choose so I can pickup and choose which data to find look at
And analyize the data to find any inesting trend. The Data is being update in different frequency Monthly, Quartely, Yearly etc.
The data can be call from the first time the data started collet some went back to the 1900.

In this project, I am to create the pipeline to ingest above data and find insigh from the data 
* Trend of the data by Country
* Breakdown of the data by Country

## Technologies
This project used tool belows.
* Prefect as data Orchestration
* DBT core as data tranformation tool for datawarehouse
* Terraform as infrastructure setup and mangament
* Docker for hosting Prefect Agent
* Googld Cloud Storage Bucket as a datalake.
* Google BigQuery as Datawarehouse
* Google Compute Engine as VM to host the pipeline
* Looker Studio for report and visualization
* Makefile for ease of reproducability

## Project Data flow
![data flow](/other/dataflow.png)
The Data flow for this project


## Reproducability
```

```

## Further Improvements
