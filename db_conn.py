import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

MY_DRIVER = os.getenv('MY_DRIVER')
MY_SERVER = os.getenv('MY_SERVER')
MY_DATABASE = os.getenv('MY_DATABASE')

connection = pyodbc.connect(f'DRIVER={MY_DRIVER};SERVER={MY_SERVER};DATABASE={MY_DATABASE};Trusted_Connection=yes;autocommit=True')

# conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};
#                        SERVER=<your_server>
#                        DATABASE=<your_database>;
#                        UID=<user>;
#                        PWD=<passwd>')
