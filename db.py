import pyodbc

server = 'test2018.database.windows.net'
database = 'TEST1'
username = 'test2018'
password = 'Siddhant13'
driver= '{ODBC Driver 17 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("INSERT INTO [dbo].[Cars] (CarName, Price) VALUES ('Toyota', 5000)")
cnxn.commit()