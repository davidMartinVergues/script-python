import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DAVID-PC;DATABASE=test-santander;Trusted_Connection=yes;autocommit=True')

# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};
#                        SERVER=<your_server>
#                        DATABASE=<your_database>;
#                        UID=<user>;
#                        PWD=<passwd>')

# cursor=connection.cursor()
# cursor.execute("SELECT * from test_santander")
# while 1:
#     row = cursor.fetchone()
#     if not row:
#         break
#     print(row)
# cursor.close()
# connection.close()