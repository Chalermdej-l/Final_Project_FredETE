import API_helper.url_module as hp
import pandas as pd
import datetime
import time
import os
from prefect import flow,task
from google.cloud import storage
from config import query_bq,clean_df
from prefect.deployments import Deployment
from prefect_gcp import GcpCredentials
from dotenv import load_dotenv

basedir=os.getcwd()
load_dotenv(os.path.join(basedir, './.env'))
gcp_credentials_block = GcpCredentials.load(os.getenv("Prefect_Credential"))



@task(name='Get_BQ_SQL',log_prints=True)
def GetBQdata(query):     
    df_bq = pd.read_gbq(query=query,
    project_id=os.getenv("Gcp_Project_id"),
    credentials=gcp_credentials_block.get_credentials_from_service_account()
    )
    return df_bq

@task(name='Get API',log_prints=True)
def getseriesid(id):
    offset = 0
    item = 1
    all_list = []
    while  offset<item:
        result = hp.category.series_category(category_id=id,limit=1000,offset=offset)

        if result is None:
            print('Result return with Noting skipping current call.')
            offset+= 1000

        elif result.ok:
            json = result.json()
            item =json['count']
            offset+= 1000
            all_list.extend(json['seriess'])
            
        else:
            print(f"Issue while calling API {result.status_code}")
            print(result.content)
            time.sleep(5)
    count_data = len(all_list)
    print(f'Done for ID {id} get total of {count_data}')
    time.sleep(1)
    return all_list,count_data

@task(name='Move archive file',log_prints=True)
def movearchive(bucket,typecheck):
    file_acrhive=  list(bucket.list_blobs())
    for file in file_acrhive:
        name = file.name
        pos = name.find('/')
        type = name[:pos]
        if type == 'staging':
            sub_pos = name.find('/',pos+1)
            sub_type = name[pos+1:sub_pos]
            if sub_type == typecheck:
                bucket.copy_blob(file,destination_bucket=bucket,new_name=name.replace('staging','archive'))
                bucket.delete_blob(name)    

@task(name='Clean data',log_prints=True)
def cleanseriesdf(data,id):
    df = pd.json_normalize(data)
    df_col = clean_df.series_col
    str_col  = clean_df.series_str_col
    int_col  = clean_df.series_int_col
    date_col = clean_df.series_date_col
    df_net = df[df_col]
    df_net[str_col] = df_net[str_col].astype('string')
    df_net[int_col] = df_net[int_col].astype('int')
    df_net['last_updated'] = df_net['last_updated'].str[:10]
    for col in date_col:
        df_net[col] = pd.to_datetime(df_net[col])

    id_listarray = []
    for key,item in id.items():
        _templistid =[key] * item
        id_listarray = id_listarray + _templistid
    df_net['category_id'] = id_listarray

    df_net = df_net.drop_duplicates()
    return df_net

@flow(name='Function call',log_prints=True)
def main():
    # Get series id base on cat id
    client = storage.Client(credentials=gcp_credentials_block.get_credentials_from_service_account())
    bucket = client.get_bucket(os.getenv("Gcs_Bucket_name"))
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d')
    query = query_bq.query_getseriesPara
    result_query = GetBQdata(query)
    indexfile =1
    item = 0
    all_list = []
    id_data = {}
    print('Moving file to archive folder')
    movearchive(bucket,'series')
    for id in result_query.values.tolist():
        result_id,count_data = getseriesid(id[0])
        all_list.extend(result_id)
        id_data[id[0]] = count_data
        item +=1

        # If call for 50 id clean the data and upload to cloud and relase the varible from memory
        if item % 50 == 0:
            print(f'Currnet item {item} uploading to cloud')
            df_series = cleanseriesdf(all_list,id_data)
            uppload_path =f'staging/series/{time_stamp}/SeriesData_{indexfile}_{time_stamp}.parquet'
            print(f'Uploading file to cloud for {time_stamp} category data.')
            bucket.blob(uppload_path).upload_from_string(df_series.to_parquet(), 'text/parquet')
            indexfile += 1
            all_list =[]
            id_data = {}
    print(f'Currnet item {item} uploading to cloud')
    df_series = cleanseriesdf(all_list,id_data)
    uppload_path =f'staging/series/{time_stamp}/SeriesData_{indexfile}_{time_stamp}.parquet'
    print(f'Uploading file to cloud for {time_stamp} category data.')

    # Upload to bucket
    bucket.blob(uppload_path).upload_from_string(df_series.to_parquet(), 'text/parquet')
    return True
# def deploy():
#     deployment = Deployment.build_from_flow(
#         flow=main,
#         name="Fred-Series"
#     )
#     deployment.apply()

if __name__ =='__main__':
    main()