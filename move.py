import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source = "C:/Users/pande/Downloads"
destination = "C:/Users/pande/downloads/Downloaded_Files"

folders = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class Filemovementhandler(FileSystemEventHandler):
    def on_created(self, event):
        print(event)
        name, ext = os.path.splitext(event.src_path)
        time.sleep(1)

        for key, value in folders.items():
            time.sleep(1)
            if ext in value:
                filename = os.path.basename(event.src_path)
                print("downloaded ", filename)

                path1 = source+"/"+filename
                path2 = destination+"/"+key
                path3 = destination+"/"+key+"/"+filename

                if os.path.exists(path2):
                    print("Folder Exists")
                    time.sleep(1)
                    if os.path.exists(path3):
                        print("File Already Exists")
                        print("Renaming the File ", filename)
                        newname = os.path.splitext(
                            filename)[0]+str(random.randint(0, 999))+os.path.splitext(filename)[1]
                        path4 = destination+"/"+key+"/"+newname
                        print("moving ", filename)
                        shutil.copy(path1, path4)
                    else:
                        print("moving ", filename)
                        shutil.move(path1, path3)

                else:
                    print("making directory")
                    os.makedirs(path2)
                    print("moving ", filename)
                    shutil.move(path1, path3)


eventhandler = Filemovementhandler()
observer = Observer()
observer.schedule(eventhandler, source, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
