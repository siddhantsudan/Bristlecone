import logging
import pyodbc

import azure.functions as func


def main(myblob: func.InputStream):
 server = 'test2018.database.windows.net'
 database = 'TEST1'
 username = 'test2018'
 password = 'Siddhant13'
 driver= '{ODBC Driver 17 for SQL Server}'
 cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
 cursor = cnxn.cursor()
 cursor.execute("INSERT INTO [dbo].[Cars] (CarName, Price) VALUES ('Jeep', 7000)")
 cnxn.commit()
 logging.info("This is a log!")
 return "Trigger is working"
