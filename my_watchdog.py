import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess
from datetime import datetime
from log_maker import logger_info,logger_error

def on_any_changes(event):
    
    logger_info.info(f" This file | {event.src_path} | has triggered an {event.event_type} event!")
    
    print(f"[{datetime.now()}] - This file |{event.src_path} | has triggered an {event.event_type} event! ")
    
    subprocess.call(".\script-excel-to-sqlerver\\app.py", shell=True)



if __name__ == "__main__":
    
    patterns = ["*.xlsx"]
    ignore_patterns = ["~*"]
    ignore_directories = True
    case_sensitive = False
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    
    my_event_handler.on_created = on_any_changes
    my_event_handler.on_deleted = on_any_changes
    my_event_handler.on_modified = on_any_changes
    my_event_handler.on_moved = on_any_changes
    
    path = ".\script-excel-to-sqlerver\excel_files"
   
    go_recursively = False
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    
    my_observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()




