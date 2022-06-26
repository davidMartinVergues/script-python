import db_conn as conn
import utils
import pandas as pd

def backup_database() -> None:
    sql_query = pd.read_sql_query('select * from [test_santander]',conn.connection) 

    df = pd.DataFrame(sql_query)
    df.to_csv (r'./backup/exported_data.csv') # place 'r' before the path name


def clean_database() -> None:
    
    cursor.execute("TRUNCATE TABLE [test_santander]")
    conn.connection.commit()
    

def insert_data_into_sqlserver(json_lis:list) -> None:
    
    for row in json_lis:
        
        if utils.validator.isValid(row):
            cursor.execute("INSERT INTO [test_santander] (field_1,field_2,field_13) values(?,?,?)",row["field_1"],row["field_2"],row["field_13"])
        else:
            print(f'validate error, type error in some fields=> {row}')
            
        
    conn.connection.commit()
    
   
if __name__ == "__main__":
    
    cursor=conn.connection.cursor()
   
    json_list = utils.read_all_files_to_json('./excel_files')

    
    if len(json_list)>0:
        backup_database()
        clean_database()
        insert_data_into_sqlserver(json_list)

    cursor.close()
    conn.connection.close()
