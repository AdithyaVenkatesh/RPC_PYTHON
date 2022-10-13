
import xmlrpc.client
import asyncio
import time



proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

async def deffsyncfunction():
    for i in range(0,20):
        await asyncio.sleep(.5)
        print("performing client actions")
    

async def quicksortclient(arr):
    result = proxy.bubbleSort(arr)
    await asyncio.sleep(0.5)
    print("Sorted array is:")
    print(result)

    return result

async def defquicksortclient(arr):
    await asyncio.sleep(4)
    result = proxy.bubbleSort(arr)
    await asyncio.sleep(1.5)
    print("Sorted array is:")
    print(result)

    return result



# async def addition(first,second):
#     data  = proxy.asyncadd(first, second)
#     return data

def synchronous():
    print("--------------------------synchronous call---------------------------- ")
    print("first we get input for addition of two numbers and then input for sort")
    print("----------------------------------------------------------------------")
    print("1.Addition of two numbers- add(a,b)")
    print("    ")
    first = input("enter the first number")
    first = int(first)
    second = input("enter the Second number")
    second = int(second)
    print("----------------------------------------------------------------------")
    print("      ")
    print("2.Sorting an Array- sort(arr)")
    print("       ")
    arr = []
    n = input("enter the array length")
    print("enter the array values")
    n = int(n)
    for i in range(0, n):
        # print(i)
        value = input()
        arr.append(int(value))
    print(arr)
    print("      ")
    print("calling add function and giving 3 seconds delay in server side and calling sort function")
    addResult = proxy.additionoftwonumbers(first, second)
    print("Sum of ",first," and ",second," is: ",addResult)
    print("calling Sort Function")
    result = proxy.bubbleSort(arr)
    print("Sorted array is:")
    print(result)

async def asynchronous():
    print("--------------------------Asynchronous call---------------------------- ")
    print("first we get input for addition of two numbers and then input for sort")
    print("----------------------------------------------------------------------")
    print("1.Addition of two numbers- add(a,b)")
    print("    ")
    first = input("enter the first number")
    first = int(first)
    second = input("enter the Second number")
    second = int(second)
    print("----------------------------------------------------------------------")
    print("      ")
    print("2.Sorting an Array- sort(arr)")
    print("       ")
    arr = []
    n = input("enter the array length")
    print("enter the array values")
    n = int(n)
    for i in range(0, n):
        # print(i)
        value = input()
        arr.append(int(value))
    print(arr)
    print("      ")
    addResult = proxy.asyadd(first, second)
    task = asyncio.create_task(quicksortclient(arr))
    print("making sorting async and calling it  ")
    print("calling add function and giving a pause of 1 second and the async function does not wait for that and it prints sorting first")

    await asyncio.sleep(1)
    print("Sum of ", first, " and ", second, " is: ", addResult)

    result = await task



async def deffsync():
    print("-------------------------- Deferred synchronous call---------------------------- ")
    print("first we get input for addition of two numbers and then input for sort")
    print("----------------------------------------------------------------------")
    print("1.Addition of two numbers- add(a,b)")
    print("    ")
    first = input("enter the first number")
    first = int(first)
    second = input("enter the Second number")
    second = int(second)
    print("----------------------------------------------------------------------")
    print("      ")
    print("2.Sorting an Array- sort(arr)")
    print("       ")
    arr = []
    n = input("enter the array length")
    print("enter the array values")
    n = int(n)
    for i in range(0, n):
        # print(i)
        value = input()
        arr.append(int(value))
    print(arr)
    print("      ")
    task = asyncio.create_task(defquicksortclient(arr))
    task2 = asyncio.create_task(deffsyncfunction())
    print("making sorting async and calling it  ")
    print("calling add function and giving a pause of 1 second and the async function does not wait for that and it prints sorting first")
    addResult = proxy.asyadd(first, second)
    await asyncio.sleep(2.5)
    print("Sum of ", first, " and ", second, " is: ", addResult)
    returnvalue = await task
    returnvalue1 = await task2



if __name__ == "__main__":
    print("1.sync")
    print("2.Async")
    print("3.Deferred Sync")
    val = int(input("select a operation to perform: "))
    print(val)
    if(val==1):
        synchronous()
    elif(val==2):
       asyncio.run(asynchronous())
    elif(val==3):
        asyncio.run(deffsync())
    else:
        print("choose the given options")






