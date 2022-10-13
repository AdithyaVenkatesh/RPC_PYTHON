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

# rename
def rename():
        val = input("Enter current File Name ")
        #print(val)
        val1 = input("Enter the file name to rename ")
        filename = val + ".txt"
        filename1 = val1 + ".txt"
        fullpath = clientpath + filename
        #print(fullpath)
        fullpath1 = clientpath + filename1
        #print(fullpath1)
        rename = proxy.rename_file(fullpath, fullpath1)
        if rename == True:
            print("renamed in Server")
        else:
            print(rename)
        if (os.path.exists(fullpath)):
            os.rename(fullpath, fullpath1)
            print("file renamed from client")
        else:
            print("The file does not exist")

# Delete
def delete():
        val = input("Enter File Name to delete ")
        #print(val)
        filename = val + ".txt"
        fullpath = clientpath + filename
        #print(fullpath)

        deleted = proxy.delete_file(fullpath)
        if deleted == True:
            print("Deleted from Server")
        else:
            print(deleted)

        if (os.path.exists(fullpath)):
            os.remove(fullpath)
            print("File deleted from Local")
        else:
            print("file not present in Local")




# Download
def download():
        val = input("Enter File Name to download ")
        #print(val)
        filename = val + ".txt"
        fullpath = clientpath + filename
        #print(fullpath)
        with open(fullpath, "wb") as handle:
            handle.write(proxy.server_send_file(val).data)
        print('File Downloaded from server and placed in Client folder')

# Upload
def upload():
        val = input("Enter File Name to upload ")
        # print(val)
        filename = val+".txt"
        # basename = str(os.path.basename(filename))
        # print(basename)

        fullpath = clientpath + filename
        # print(fullpath)
        if (os.path.exists(fullpath)):
            print("file Created uploading to server")
            # Upload
            with open(fullpath, "rb") as handle:
                binary_data = xmlrpc.client.Binary(handle.read())
                print(binary_data)
                data = proxy.server_receive_file(binary_data, fullpath)
                #print(data)
            print('file uploaded to server')

        else:
            print("The file does not exist")
            x = input("do you want to create the file ( y/n)  ")
            if x=='y':
                with open(filename, 'w') as fp:
                    pass
                with open(fullpath, "rb") as handle:
                    binary_data = xmlrpc.client.Binary(handle.read())
                    print(binary_data)
                    data = proxy.server_receive_file(binary_data, fullpath)
                    #print(data)
                print('File uploaded to server')
            else:
                print("exiting")



if __name__ == "__main__":
    print("1.Upload")
    print("2.Download")
    print("3.Delete")
    print("4.Rename")
    val = int(input("select a operation to perform: "))
    print(val)
    if(val==1):
        upload()
    elif(val==2):
        download()
    elif(val==3):
        delete()
    elif(val==4):
        rename()
    else:
        print("choose the given options")
