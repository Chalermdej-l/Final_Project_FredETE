# End To End Fred API Data Pipeline

## Table of contents

* [Problem Statement](#problem-statement)
* [Technologies](#technologies)
* [Project Data flow](#project-data-flow)
  - [(1) Ingest the Data via API](#1-ingest-the-data-via-api)
  - [(2) Load data via External table](#2-load-data-via-an-external-table)
  - [(3) Data tranformation](#3-data-tranformation)
  - [(4) Visualize data to find insight](#4-visualize-data-to-find-insight)
  - [(5)(6) Schedule daily data ingest and tranformation](#56-schedule-daily-data-ingest-and-transformation)
* [Reproducability](#reproducability)
  - [Step 1: Create infratructure](#step-1-create-infrastructure)
  - [Step 2: Connect to VM and install dependency](#step-2-connect-to-the-vm-and-install-the-dependency)
  - [Step 3: Deploy code to prefect](#step-3-deploy-code-to-prefect)
  - [Step 4: Run the script](#step-4-run-the-script)
* [Further Improvements](#further-improvements)

## Problem Statement

This project implements concepts learn from [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) course.
To build a pipeline to ingest the data store them in a datalake and process them into the Data warehouse.

The Data used in this project is from [FRED Economic Data](https://fred.stlouisfed.org/docs/api/fred). Using the FRED API to call the data using Python with Prefect Orchestration.
Store them in Google Cloud Storage Bucket and Use DBT to transform data into BigQuery and connect with Looker Studio to find insight from the data.

There are multiple data in FRED Economic data. I want to create a pipeline to ingest these databases base on the [topic choose.](/DBT/seeds/series_group.csv)
Analyze the data to find any interesting trends. The Data is being updated in different frequencies Monthly, quarterly, Yearly, etc.
Some of the data went back to the 1990.

In this project, I aim to create the pipeline to ingest the above data and create report to find the
- The trend of the data
- Breakdown of the data by Country

## Technologies

This project used the tool below.

- Perfect as data Orchestration
- DBT core as a data transformation tool for data warehouse
- Terraform as infrastructure setup and management
- Docker for hosting Prefect Agent
- Google Cloud Storage Bucket as a data lake.
- Google BigQuery as a Data warehouse
- Google Compute Engine as VM to host the pipeline
- Looker Studio for report and visualization
- Makefile for ease of reproducibility

## Project Data flow

![/other/image/dataflow.PNG](/other/image/dataflow.PNG)

The Data flow for this project

### (1) Ingest the Data via API

The data is called from [FRED API](https://fred.stlouisfed.org/docs/api/fred/#API).

We first need to get the category id from for all the topics. But FRED does not have an endpoint to get all the category id so to get this data we need to scape it from the [Category](https://fred.stlouisfed.org/categories) by ussing this [Python script](/flows/DBT_ingest.py).

Checking the [Robots.txt](https://fred.stlouisfed.org/robots.txt) Fred does not disallow scraping of this data.

After we ran the script and get the category id we then can use the id to call [Cagetory Series](https://fred.stlouisfed.org/docs/api/fred/category_series.html) endpoint to get all the series associated with the category.

After we get the series id we can call [Maps API - Series Group Info](https://fred.stlouisfed.org/docs/api/geofred/series_group.html) to get the group id of the series not all series IDs have group id however. So to reduce the time I have extract the series with the group id and saved them in this [CSV](/DBT/seeds/series_group.csv).

This file use a column Active to indicate which data should be call daily by the script.

![active](/other/image/active.png)


then we use the series group id to call the [Maps API - Series Data](https://fred.stlouisfed.org/docs/api/geofred/series_data.html) endpoint which will return the data by country for the id we requested.

### (2) Load data via an External table

The data is stored in google cloud storage in stagging folder for series and category data as there could be new categories or series id added

![/other/image/bucket1.png](/other/image/bucket1.png)

Then move to the archive folder after the next day's data point is called.

![/other/image/bucket2.png](/other/image/bucket2.png)

For Map data, we store them in the Map folder.

We use Google BigQuery to connect to the data using external table data sources this connection is defined in [Terraform](/infra/bq.tf) file.
The dataset is seperate into 2 datasets for development and production.

### (3) Data tranformation

This project uses [DBT](/DBT) for data transformation the model is separated into 2 stages core and stagging. In staging this is for casting the data type into the correct type and in core use this to join all the tables from stagging and from seed into one table

### (4) Visualize data to find insight

Use Looker Studio to connect to the BigQuery data warehouse and create reports to find trends and insight
![/other/image/bucket1.png](/other/image/Dashboard.png)

[Link to the Dashboard](https://lookerstudio.google.com/reporting/88eb65d7-c3ec-44b1-898a-55ded00812a0)

### (5)(6) Schedule daily data ingest and transformation

Used prefect as an orchestrator tool to schedule the daily call of our script and data transformation using the deployment functionality.

## Reproducibility

Prerequisite:
To reproduce this project you would need the below account

1. [Google Cloud Account](/other/gcpsetup)
2. [Prefect Cloud](/other/prefectsetup)
3. [Fred's Economic](/other/fredsetup)

You also need below package

1. [Makefile](https://pypi.org/project/make/) `pip install  make`
2. [Gcloud CLI](https://pypi.org/project/gcloud/) `pip install gcloud`
3. [Terraform](https://developer.hashicorp.com/terraform/downloads)
4. [DotEnv](https://pypi.org/project/python-dotenv/) `pip install python-dotenv`

### Step 1: Create infrastructure

Clone this project

```
git clone https://github.com/Chalermdej-l/Final_Project_FredETE
```

Access the clone directory

```
cd Final_Project_FredETE
```

Input the credential create in the `Prerequisite` step into the [.env](/.env) file

![env](/other/image/envcred.png)

Input the credential.json create in Google Cloud Account into the folder cred

![credential](/other/image/gcpsetup8.png)


Run the following command using Makefile depending on your system

```
make update-yml-window
```

```
make update-yml-linix
```

This code will populate the credential in the YAML file using the credential input in the [.env](/.env) file

Next, let's create the infrastructure to run

```
make infra-setup
```

This command will setup the terraform and run the plan to check for any error

![/other/image/repeoducesetup1.png](/other/image/repeoducesetup1.png)

To create the resource please run

```
make infra-create
```

This will create BigQuery, Google Cloud Storage Bucket, VM Instances

Once the code is done please go to the [VM Instances](https://console.cloud.google.com/compute/instances) and copy the external IP

![/other/image/repeoducesetup3.png](/other/image/repeoducesetup3.png)

Please input the External IP into the .env file we will need this to connect to the VM

### Step 2: Connect to the VM and install the dependency

Open a new terminal and navigate to the clone directory and run

```
make vm-connect
```

This script will connect to the VM. There might be a question asking to save this host into the known host please select `yes`.

After we are in the VM please clone the repository again

```
git clone https://github.com/Chalermdej-l/Final_Project_FredETE
```

Then navigate to the clone folder

```
cd Final_Project_FredETE
```

Run the below command to install Python Make and dotenv

```
sudo apt-get update -y
sudo apt install python3-pip -y
```
```
sudo pip install make
sudo pip install python-dotenv
```

Then go back to the local terminal and run

```
make vm-copycred
```

This will copy the credential we input in .env and the credential.json we download to the VM

Go back to the VM terminal and run the below command to setup the credential

```
make update-yml-linix
```

Then run the below command to install Docker and Docker-Compose

```
make vm-setup
```

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

```
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```


After finishing run the below command to create the docker image and spin up the prefect agent in the background

```
make docker-build
```
```
make docker-up
```

### Step 3: Deploy code to prefect

After the docker is running please run

```
make deployment-create
```
```
make deployment-dbtprod
```
This will setup the schedule daily script in prefect

![/other/image/prefectschedule.png](/other/image/prefectschedule.png)

To set up the data to call the script please run

```
make dbt-ingest
```

This will run the DBT seed and set up the data for the script to run

### Step 4: Run the script

Please go to [Prefect](https://app.prefect.cloud/auth/login) and run the job in below order to start ingesting the data

1. Fred-Category

2. Fred-Series

3. Fred-MapAPI

4. DBT-Daily-prod

After finish running all the jobs the data will be ingested into [BigQuery](https://console.cloud.google.com/bigquery)

## Further Improvements

- Implement CI/CD
- Explore other Endpoint of the API
