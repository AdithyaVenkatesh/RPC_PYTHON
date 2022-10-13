from cmath import log
import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os
import time
import asyncio

serverpath = './'
def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

def server_receive_file(arg,filename):
    basename = str(os.path.basename(filename))
    fullpath = serverpath+basename
    print(fullpath)
    with open(fullpath, "wb") as handle:
        handle.write(arg.data)
        print(arg.data)
        return True

def server_send_file(filename):
  basename = str(os.path.basename(filename))
  print(basename)
  fullName = serverpath+basename+'.txt'
  print(fullName)
  if (os.path.exists(fullName)):
      with open(fullName, "rb") as handle:
          return xmlrpc.client.Binary(handle.read())
  else:
      return ("The file does not exist in server check file name")



def delete_file(filename):
    basename = str(os.path.basename(filename))
    print(basename)
    fullpath = serverpath + basename
    print(fullpath)
    if (os.path.exists(fullpath)):
        os.remove(fullpath)
        return True
    else:
        return ("The file does not exist")

def rename_file(old,new):
    basename = str(os.path.basename(old))
    basename1 = str(os.path.basename(new))
    fullpath = serverpath + basename
    fullpath1 = serverpath+ basename1
    print(fullpath)
    if (os.path.exists(fullpath)):
        os.rename(fullpath,fullpath1)
        return True
    else:
        print("else part")
        return ("The file does not exist")

# def partition(arr, low, high):
#     i = (low -1)
#     pivot = arr[high]
#
#     for j in range(low, high):
#
#         if arr[j] <= pivot:
#
#             i = i+ 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
#
# def quickSort(arr, low, high):
#     print("quick sort")
#     if len(arr) == 1:
#         return arr
#     if low < high:
#
#         pi = partition(arr, low, high)
#
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)


def bubbleSort(arr1):
    arr = arr1
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def additionoftwonumbers(first,last):
    time.sleep(3)
    return first+last

def asyadd(first,last):
    return first+last



server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(today, "today")
server.register_function(server_receive_file, "server_receive_file")
server.register_function(server_send_file, "server_send_file")
server.register_function(delete_file, "delete_file")
server.register_function(rename_file, "rename_file")
server.register_function(bubbleSort, "bubbleSort")
server.register_function(additionoftwonumbers, "additionoftwonumbers")
server.register_function(asyadd, "asyadd")
server.serve_forever()

