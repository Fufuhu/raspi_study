from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import os
import time

class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print("%sが作成されました。" % filename)
    
    def on_modified(self, event):
        pass
    
    def on_deleted(self, event):
        pass

if __name__ in '__main__':
    while True:
        event_handler = ChangeHandler()

        target_dir = os.getenv('TARGET_DIR')
        print('TARGET_DIR: ' + target_dir)
        if target_dir is None:
            exit(1)
        observer = Observer()
        observer.schedule(event_handler=event_handler, path=target_dir, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
            