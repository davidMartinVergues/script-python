import pandas as pd
import json,sys,itertools,pyodbc
import validator
from os import listdir
from os.path import isfile, join

def parse_file_to_json(path:str) -> list:
    
    df = pd.read_excel(path)
    
    json_str_list = df.to_json(orient = 'records')
    json_list = json.loads(json_str_list)
    
    return json_list

def read_all_files_to_json(path:str)-> list:
    
    only_xlsx_files = [join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.lower().endswith('.xlsx') and not f.lower().startswith('~')]
    
    if len(only_xlsx_files) > 0:
        
        all_files_to_json= []
        data = []
        
        for files in only_xlsx_files :
            
            try:
               all_files_to_json.append(parse_file_to_json(files))
            except BaseException as err:
                print('\nsomething went wrong!\n')
                print(f'{sys.exc_info()}\n')
                print(f'{err} \n')
                
        
        data = list(itertools.chain(*all_files_to_json))
            
        return data
    else:
       raise Exception('excel file not found')
