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

(1) Ingest the Data via API
We call the data from [API](https://fred.stlouisfed.org/docs/api/fred/#API). We first need to get the category id from for all the topic FRED do not have endpoint to get all the category id from the API so to get this data we need to scape it from the [Category](https://fred.stlouisfed.org/categories) using [Python script](flows/Fred_Category_Scape.py). Checking the [Robots.txt](https://fred.stlouisfed.org/robots.txt) Fred do not disallow scapping of this data. After we get the id we then call the [Cagetory Series](https://fred.stlouisfed.org/docs/api/fred/category_series.html) endpoint to get all the series accoiate with the category. After we get the series id we call [Maps API - Series Group Info](https://fred.stlouisfed.org/docs/api/geofred/series_group.html) to get the group id of the series not all series id have group id.I have call the series with group id and save thme in this [CSV](/DBT/seeds/series_group.csv) then we use the series id to cal the [Maps API - Series Data](https://fred.stlouisfed.org/docs/api/geofred/series_data.html) endpoint this will return the data by country for the series id we requestd.

(2) Load data via External table


## Reproducability
```

```

## Further Improvements
