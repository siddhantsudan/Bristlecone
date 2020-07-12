import logging
import pyodbc
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    server = 'test2018.database.windows.net'
    database = 'TEST1'
    username = 'test2018'
    password = 'Siddhant13'
    driver= '{ODBC Driver 17 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT TOP 1 * FROM [dbo].[Total] ORDER BY Total DESC")
    records = cursor.fetchall()
    cnxn.commit()
    return func.HttpResponse(f"{records[0][0]}")
