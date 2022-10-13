from pickle import TRUE
import xmlrpc.client
import datetime
# import time module, Observer, FileSystemEventHandler
import time
import os
import sys
import logging

import watchdog.utils.dirsnapshot
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
clientpath = './'


def on_created(event):

    filename = event.src_path
    print("filename",filename)
    basename = str(os.path.basename(filename))
    print(basename)

    if "~" in basename:
        print("dummy create")

    else:
        fullpath = clientpath+basename

        print("file Created uploading to server")
        # Upload
        with open(fullpath, "rb") as handle:
            binary_data = xmlrpc.client.Binary(handle.read())
            print(binary_data)
            data = proxy.server_receive_file(binary_data, fullpath)
            print(data)


def on_deleted(event):
    print("file is getting Deleted while modifying")
    filename = event.src_path
    filename = event.src_path
    basename = str(os.path.basename(filename))

    fullpath = clientpath + basename

    # Delete
    deleted = proxy.delete_file(fullpath)
    print(deleted)

def on_modified(event):
    # print("file is getting Deleted while modifying")

    filename = event.src_path
    basename = str(os.path.basename(filename))
    print("file name is : ",filename)
    if ".txt" in basename:
        print("basename is ",basename)
        fullpath = clientpath + basename
        with open(fullpath, "rb") as handle:
            binary_data = xmlrpc.client.Binary(handle.read())
            data = proxy.server_receive_file(binary_data,fullpath)
                # print(data)

    else:
        print('it creates a temporary file .gooutputstream')
  

    # # modified is same as upload


def on_moved(event):
    print("moved")
    print(event.src_path)
    # print(event_handler.logger)
    # rename
    # Rename = proxy.rename_file('test.txt','rename.txt')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()


    event_handler.on_created = on_created
    event_handler.on_deleted = on_deleted
    event_handler.on_moved= on_moved
    event_handler.on_modified= on_modified



    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
# Download
# with open('download.txt', "wb") as handle:
#     handle.write(proxy.server_send_file().data)


    # today = proxy.today()
    # converted = datetime.datetime.strptime(today.value, "%Y%m%dT%H:%M:%S")
    # print("Today: %s" % converted.strftime("%d.%m.%Y, %H:%M"))

# convert the ISO8601 string to a datetime object

