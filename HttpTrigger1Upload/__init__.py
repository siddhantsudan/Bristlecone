import logging
import xlrd 
import pandas as pd 
import ssl
import pyodbc
#import cgi, os
#import cgitb; cgitb.enable()
import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient
#from azure.storage.blob.baseblobservice import BaseBlobService
from azure.storage.blob import generate_blob_sas
from io import StringIO
#from azure.storage.blob import BlockBlobService
#from azure.storage.blob import baseblobservice
#from azure.storage.blob import BlobPermissions
#from datetime import datetime, timedelta

#import xlrd 

def main(req: func.HttpRequest) -> func.HttpResponse:
    #form = cgi.FieldStorage()
    #fileitem = form['filename']
    #file=  req.files.get('file')
    file=  req.files.get('file')
    connect_str="DefaultEndpointsProtocol=https;AccountName=upload2017;AccountKey=hRF/4rD/AV/WF3I1srQgHipU0imTKm6nB/4Rk9MwaQlTYPe5AwF1vsfIgow0yb6gYyeTeaKcyzWSeFFQX/DwTQ==;EndpointSuffix=core.windows.net"
    container="test2019"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client =blob_service_client.get_blob_client(container=container,blob=file.filename)
    blob_client.upload_blob(file)
    server = 'test2018.database.windows.net'
    database = 'TEST1'
    username = 'test2018'
    password = 'Siddhant13'
    driver= '{ODBC Driver 17 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    
    blob = BlobClient(account_url="https://upload2017.blob.core.windows.net",container_name="test2019",blob_name=file.filename,credential="hRF/4rD/AV/WF3I1srQgHipU0imTKm6nB/4Rk9MwaQlTYPe5AwF1vsfIgow0yb6gYyeTeaKcyzWSeFFQX/DwTQ==")
    #blob_data = blob.download_blob()
    #blob_data = blob.uri
    account_name="upload2017"
    account_key="hRF/4rD/AV/WF3I1srQgHipU0imTKm6nB/4Rk9MwaQlTYPe5AwF1vsfIgow0yb6gYyeTeaKcyzWSeFFQX/DwTQ=="
    #blob_service = BaseBlobService(account_name=account_name,account_key=account_key)
    #sas_token = blob_service.generate_blob_shared_access_signature(container, file.filename, permission=BlobPermissions.READ, expiry=datetime.utcnow() + timedelta(hours=1))
    #blob_url_with_sas = blob_service.make_blob_url(container, file.filename, sas_token=sas_token)
    ssl._create_default_https_context = ssl._create_unverified_context
    url="https://upload2017.blob.core.windows.net/test2019/Value.xlsx"
    #blob_service=BlockBlobService(account_name=account_name,account_key=account_key)
    
    #df = pd.read_excel(blob_service.get_blob_to_bytes("test2019",file.filename), sheet_name=0, header=0)
    df = pd.read_excel(url, sheet_name=0, header=0)
    #print(df['Values'].sum())
    total=df['Values'].sum()
    #for i in range(1,sheet.nrows): 
     #total=total+float(sheet.cell_value(i, 0))
    cursor.execute("INSERT INTO [dbo].[Total] (Total) VALUES ("+str(total)+")")
    cnxn.commit()
    
    #logging.info("This is a log!")
    
    #filename="Empty"
    #for input_file in req.files.values():
        #filename = input_file.filename
        #contents = input_file.stream.read()
    
# Test if the file was uploaded
    #if file.filename:
     #fn = os.path.basename(fileitem.filename)
     #open('/tmp/' + fn, 'wb').write(fileitem.file.read())
     #wb = xlrd.open_workbook('/tmp/' + fn, 'wb') 
     #sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
     #print(sheet.cell_value(0, 0)) 
     #message = 'The file "' + fn + '" was uploaded successfully'
    #else:
     #message = 'No file was uploaded'
    #print(file.filename)
    logging.info(file.filename)
    return func.HttpResponse(f"Hello {file.filename}!{total}")
  
