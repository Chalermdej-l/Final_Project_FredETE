# End To End Fred API Data Pipeline
## Table of contents
* [Problem Statement](#problem-statement)
* [Technologies](#technologies)
* [Project Data flow](#project-data-flow)
  - [(1) Ingest the Data via API](#1-ingest-the-data-via-api)
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
![data flow](/other/image/dataflow.PNG)
The Data flow for this project

### (1) Ingest the Data via API
The data is call from [API](https://fred.stlouisfed.org/docs/api/fred/#API). We first need to get the category id from for all the topic FRED do not have endpoint to get all the category id from the API so to get this data we need to scape it from the [Category](https://fred.stlouisfed.org/categories) using [Python script](flows/Fred_Category_Scape.py). Checking the [Robots.txt](https://fred.stlouisfed.org/robots.txt) Fred do not disallow scapping of this data. After we get the id we then call the [Cagetory Series](https://fred.stlouisfed.org/docs/api/fred/category_series.html) endpoint to get all the series accoiate with the category. After we get the series id we call [Maps API - Series Group Info](https://fred.stlouisfed.org/docs/api/geofred/series_group.html) to get the group id of the series not all series id have group id.I have call the series with group id and save thme in this [CSV](/DBT/seeds/series_group.csv) then we use the series id to cal the [Maps API - Series Data](https://fred.stlouisfed.org/docs/api/geofred/series_data.html) endpoint this will return the data by country for the series id we requestd.

### (2) Load data via External table
The data is store in google cloud storage in stagging folder for series and cateogry data as there could be new category or series id added

![Storage](/other/image/bucket1.png)

Then move to archive folder after the next day data point is call.

![Archive](/other/image/bucket2.png)

For Map data we store them in Map folder.

We use Google BigQuery to call the data using external table data sources this connection is define in [Terraform](/infra/bq.tf) file.
I seperate the dataset into 2 dataset for development and production.

### (3) Data tranformation
This project use [DBT](/DBT) for data tranformation the model is seperate in 2 stage core and stagging. In stagging this is for casting the data type into the correct type and in core use this to join all the table from stagging and from seed into one table

### (4) Visualize data to find insight
Use Looker studio to connect to BigQuery data warehouse and create report to find trend and insight


[Dashboard](https://lookerstudio.google.com/reporting/88eb65d7-c3ec-44b1-898a-55ded00812a0)


### (5)(6) Schedule daily data ingest and tranformation
Used prefect as an orchestrator tool to schedule the daily call of our script and data tranformation using the deployment functionality.

## Reproducability

Prerequisite:
To reproduce this project you would need the below acount

1.[Google Cloud Account](/other/gcpsetup/)

2.[Prefect Cloud](/other/prefectsetup/)

3.[Fred Economic](/other/fredsetup/)

You also need below package

1.[Makefile](https://pypi.org/project/make/) ``` pip install  make  ```

2.[Gcloud CLI](https://pypi.org/project/gcloud/) ``` pip install gcloud ```

3.[Terraform](https://developer.hashicorp.com/terraform/downloads)

4.[DotEnv]([pip install python-dotenv](https://pypi.org/project/python-dotenv/) ``` pip install python-dotenv ```

### Step 1: Create infratructure 

Clone this project 
``` 
git clone https://github.com/Chalermdej-l/Final_Project_FredETE 
```

Access the clone directory
``` 
cd Final_Project_FredETE 
``` 

Input the credential create in the `Prerequisite` step into the [.env](/.env) file

Run the following command using Makefile depend on your system

``` 
make update-yml-window 
``` 

``` 
make update-yml-linix 
``` 

This code will populate the credential in yaml file using the credential input in [.env](/.env) file

Next let create the infratructure run

``` 
make infra-setup 
``` 

This command will setup the terraform and ran plan to check for any error

![Terraform](/other/image/repeoducesetup1.png)

To create the resouce please run

``` 
make infra-create 
``` 

This will create BigQuery, Google Cloud Storage Bucket, VM Instances

Once the code done please go to the [VM Instances](https://console.cloud.google.com/compute/instances) and copy the external IP

![Terraform](/other/image/repeoducesetup3.png)

Please input the External IP into the .env file we will need this to connect to the VM

### Step 2: Connect to VM and install dependency

Open a new terminal and naviage to the clone directory and run

``` 
make vm-connect 
``` 

This script will connect to the VM. There might be a questoin asking to save this host into the known host please select `yes`.

After we are in the VM please clone the repository again

``` 
git clone https://github.com/Chalermdej-l/Final_Project_FredETE 
```

Then navigate to the clone folder 

``` 
cd Final_Project_FredETE 
``` 

Run the below commad to install python Make and dotenv
 ```
sudo apt-get update -y
sudo apt install python3-pip -y
sudo pip install make
sudo pip install python-dotenv
  ```
Then go back to the local terminal and run

  ```
  make vm-copycred  
  ```
  
This will copy the credential we input in .env and the credential.json we download to the VM

Go back to the VM terminal run below command to setup the credential

```
make update-yml-linix
```

Then run below command to install Docker and Docker-Comopse

```
make vm-setup
make vm-setupdocker
```

After finish run below commnad to create the docker image and spin up the prefect agent in the background
```
make docker-build
make docker-up 
```

### Step 3: Deploy code to prefect

After the docker is running please run
```
make deployment-create
make deployment-dbtprod
```
This will setup the schedule daily script in prefect

![Terraform](/other/image/prefectschedule.png)

To setup the data to call the script please run
```
make make dbt-ingest
```
This will run DBT seed and setup the data for the script to run

### Step 4: Run the script

Please go to [Prefect](https://app.prefect.cloud/auth/login) and run the job in below order to start ingest the data
1.Fred-Category
2.Fred-Series
4.Fred-MapAPI
5.DBT-Daily-prod

After finish running all the job the data will be ingest into [BigQuery](https://console.cloud.google.com/bigquery)




## Further Improvements
