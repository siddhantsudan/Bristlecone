#import xlrd
import pandas as pd 
import requests
#import ssl

#context = ssl._create_unverified_context()
#urllib.urlopen("https://no-valid-cert", context=context)
#ssl._create_default_https_context = ssl._create_unverified_context
#url="https://upload2017.blob.core.windows.net/test2019/Value.xlsx"
#resp = requests.get(url)
sas_token = blob_service.generate_blob_shared_access_signature(container_name, blob_name, permission=BlobPermissions.READ, expiry=datetime.utcnow() + timedelta(hours=1))
blob_url_with_sas = blob_service.make_blob_url(container_name, blob_name, sas_token=sas_token)

df = pd.read_excel(resp.content, sheet_name=0, header=0)
print(df['Values'].sum())
#loc = ("/Users/Siddhant/Desktop/Bristlecone/Value.xlsx") 
  
#wb = xlrd.open_workbook(loc) 
#sheet = wb.sheet_by_index(0) 
#sheet.cell_value(0, 0) 
#total=0
#for i in range(1,sheet.nrows): 
 #   total=total+float(sheet.cell_value(i, 0))
#print(total)