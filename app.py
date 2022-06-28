import db_conn as conn
import utils
import pandas as pd
from datetime import datetime
from log_maker import logger_info,logger_error

def backup_database() -> None:
    
    logger_info.info('backup database')
    
    dt = datetime.now()
    date = dt.strftime("%d_%m_%y_%H_%M_%S_%f")
    
    
    compression_opts = dict(method='zip',
                        archive_name=f'exported_data_{date}.csv')
    
    try:
        sql_query = pd.read_sql_query('select * from [test_santander]',conn.connection)
        df = pd.DataFrame(sql_query)
        
        df.to_csv('.\script-excel-to-sqlerver\\backup\\'+date+'_.zip', index=False,
            compression=compression_opts)
        logger_info.info('retrieving information from database - successful -')
        logger_info.info('ZIP created - successful -')
    except BaseException as err:
        logger_error.error('something went wrong on backup database', exc_info=True)
        logger_error.error(err)
        logger_info.info('something went wrong on backup database')
        
        

def clean_database() -> None:
    
    logger_info.info('cleaning database')
    
    try:
        cursor.execute("TRUNCATE TABLE [test_santander]")
        conn.connection.commit()
        
        logger_info.info('- succesfull - ')
    except BaseException as err:
        logger_error.error('something went wrong cleaning database',exc_info=True)
        logger_error.error(err)
        logger_info.info('something went wrong cleaning database')
        
    
    

def insert_data_into_sqlserver(json_lis:list) -> None:
    
    logger_info.info('Adding data into database')
    
    for row in json_lis:
        
        if utils.validator.isValid(row):
            try:
                cursor.execute("INSERT INTO [test_santander] (field_1,field_2,field_13) values(?,?,?)",row["field_1"],row["field_2"],row["field_13"])
            except BaseException as err:
                logger_error.error(f'Data not added into database - {row}', exc_info=True)
                logger_error.error(err)
                logger_info.info(f'Data not added into database - {row}')
        else:
            logger_error.error(f'validation error, type error in some fields=> {row}')
            print(f'validation error, type error in some fields=> {row}')
            
    logger_info.info(f'Adding finished')    
    conn.connection.commit()
    
   
if __name__ == "__main__":
    
    cursor=conn.connection.cursor()
   
    json_list = utils.read_all_files_to_json('.\script-excel-to-sqlerver\excel_files')

    
    if len(json_list)>0:
        backup_database()
        clean_database()
        insert_data_into_sqlserver(json_list)

    cursor.close()
    conn.connection.close()
