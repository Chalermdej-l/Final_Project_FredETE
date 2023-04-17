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
def cleandata(df,groupid):
    str_col = ['region','code','series_id']
    df_map = pd.json_normalize(df,record_path=['data'],meta=['date'])
    df_map['date'] = pd.to_datetime(df_map['date'])
    df_map['groupid'] = int(groupid)            
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
            para_mindate     = current_date
            para_maxdate     = current_date
        else:
            para_mindate     = api_para[5]
            para_maxdate     = current_date

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
        dict_df= {}
        list_df =[]

        for day in time_para:
            dict_df['date'] = day
            dict_df['data'] = data_date[day]
            list_df.append(dict_df)
            dict_df= {}
        df_map =  cleandata(list_df,para_seriesgroup)
        uppload_path =f'map/{para_seriesgroup}/MapData_{para_seriesgroup}_{para_mindate}_{para_maxdate}.parquet'
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