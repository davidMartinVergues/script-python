import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess
from datetime import datetime

def on_created(event):
    print(f"[{datetime.now()}] - {event.src_path} has trigger an event! ")
    subprocess.call("app.py", shell=True)





if __name__ == "__main__":
    
    patterns = ["*.xlsx"]
    ignore_patterns = ["~*"]
    ignore_directories = True
    case_sensitive = False
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_created
    my_event_handler.on_modified = on_created
    my_event_handler.on_moved = on_created
    
    path = "./excel_files"
    
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




