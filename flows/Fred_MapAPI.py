import API_helper.url_module as hp
import pandas as pd
import time
import datetime
import os
from prefect.deployments import Deployment
from prefect import flow,task
from google.cloud import storage
from config import query_bq 
from prefect_gcp import GcpCredentials
from dotenv import load_dotenv


basedir=os.getcwd()
load_dotenv(os.path.join(basedir, './.env'))

gcp_credentials_block = GcpCredentials.load(os.getenv("Prefect_Credential"))

@task(name='Get_BQ_SQL_Map',log_prints=True)
def GetBQdata(query): 

    df_bq = pd.read_gbq(query=query,
    project_id=os.getenv("Gcp_Project_id"),
    credentials=gcp_credentials_block.get_credentials_from_service_account()
    )
    return df_bq


@task(name='Get_API_Map',log_prints=True)
def getApiMap(para_regiontype,para_seriesgroup,para_season,para_unit,para_frequency,para_mindate,para_maxdate):

        print(f'Calling the API for {para_seriesgroup} ...')
        result = hp.map.regional(
            file_type ='json' \
            ,series_group = para_seriesgroup \
            ,region_type = para_regiontype \
            ,date = para_maxdate \
            ,start_date = para_mindate
            ,season=para_season \
            ,units=para_unit
            ,frequency = para_frequency
        )
        if result is None:
            print(f'Result return with None skipping currnt call for {para_seriesgroup} period {para_mindate} - {para_maxdate}')
            return None

        elif result.ok:
            try:
                data_all = result.json()
                data_date =data_all['meta']['data']
                return data_date    

            except Exception:
                print(f'An error occured {Exception}')
                return None

        else:
            print(f'An error occur {result.status_code}.')
            print(f'An error occur {result.content}.')
            print('Waiting for 5 sec.')
            return 'retry'

@task(name='Cleandata_Map',log_prints=True)
def cleandata(df,date,groupid):
    str_col = ['region','code','series_id']
    df_map = pd.json_normalize(df[date])
    df_map['date'] = datetime.datetime.strptime(date,"%Y-%m-%d")
    df_map['groupid'] = groupid            
    df_map[str_col] = df_map[str_col].astype('string')
    df_map['value'] = df_map['value'].astype('float')
    return df_map

@flow(name='Function call Map',log_prints=True)
def main(version='initial'):    
    series_parameter = GetBQdata(query_bq.query_getMapPara)
    client = storage.Client(credentials=gcp_credentials_block.get_credentials_from_service_account())
    bucket = client.get_bucket(os.getenv("Gcs_Bucket_name"))

    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    for api_para in series_parameter.values.tolist():
        para_regiontype  = api_para[0][0]
        para_seriesgroup = api_para[1][0]
        para_season      = api_para[2][0]
        para_unit        = api_para[3][0]
        para_frequency   = api_para[4][0]
        if version=='daily':
            para_mindate     = api_para[6]
            para_maxdate     = current_date
        else:
            para_mindate     = api_para[5]
            para_maxdate     = api_para[6]

        retry = 0
        while retry <3:
            data_date =   getApiMap(para_regiontype,para_seriesgroup,para_season,para_unit, para_frequency,para_mindate,para_maxdate)
            if data_date == 'retry':
                retry+= 1
                print(f'Retry the current call. Current retry {retry}')
                continue
            elif data_date ==None:
                print(f'Skpping the call for {para_seriesgroup}')
                continue
            else:
                break
        
        if  retry ==3:
            print(f'Error occur skipping {para_seriesgroup}')
            continue
        
        print(f'Uploading file to cloud for {para_seriesgroup}')   
        time_para = list(data_date.keys())
        for day in time_para:
            df_map =  cleandata(data_date,day,para_seriesgroup)
            uppload_path =f'map/{para_seriesgroup}/MapData_{para_seriesgroup}_{day}.parquet'
            bucket.blob(uppload_path).upload_from_string(df_map.to_parquet(), 'text/parquet')
            time.sleep(1)
    print('Finish running the function.')
    return True



def deploy():
    deployment = Deployment.build_from_flow(
        flow=main,
        name="Fred-MapAPI"
    )
    deployment.apply()

if __name__ =='__main__':
    deploy()