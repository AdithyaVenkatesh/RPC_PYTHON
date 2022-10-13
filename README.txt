CSE 5306 Distributed Systems Spring 2022 Project 1

Adithya Venkatesh (1002032198,axv2198@mavs.uta.edu)

Part-1 

Downloaded UTM Virtual machine and Installed Ubuntu.

Install Python in Ubuntu:

sudo apt install python3 (press enter)
sudo apt install python3-pip (press enter)
sudo apt install watchdog ( to install watchdog for part 3)


Steps to place the folder

Folder Name : DistributedSystems
Sub Folder : DistributedSystems/Client , DistributedSystems/Server
unzip the Folder (DistributedSystems) and place it in Desktop

Setting up Server:
--------------------
1. open Server folder( DistributedSystems/Server) and open Terminal for Server Folder
2. There will be one Server file (DistributedSystems/Server/server.py)
3. To start the server Type: python3 server.py
4. The server will be up and running. 


Setting up Client
----------------------
- open Client Folder and open Terminal for Client folder 

-------------------------
Part 2 of the project : 
--------------------------

file name : client.py

To start the client type : python3 client.py

There will be 4 options to ( Upload, Download,Delete,Rename)

1.Upload
2.Download
3.Delete
4.Rename

Steps to Upload:
- type in terminal to start client :   python3 client.py
- Select 1 to upload the file. 
- It will prompt for file name give the file name and if file is not present it will create a file in Client and take a backup in server

Step to Download:

- Delete the file which you uploaded only in client
- type in terminal to start client:    python3 client.py 
- select option 2
- give the file name which you have uploaded if file is present it will bring it from server 

Steps to Rename:

- type in terminal to start client:    python3 client.py 
- It will prompt for current file name and new file name, once both are given it will be renamed both in server and client

Steps to Delete

- type in terminal to start client:    python3 client.py 
- It will prompt for file name to be deleted, give the file name. file in server and client will be deleted.


-------------------------
Part 3 of the project : 
--------------------------

file name : client.py
Clear the terminal with code:   Clear
To start the client type : python3 client1.py 
the client should be running and server should be running as well
open one more terminal in Client path to do the below steps 


Steps to check Part3 :

-  open one more terminal in the Client folder and we are going to create, modify and delete a file and it will automatically do it in client and Server.

Type the following commands

CREATE A FILE

cat >> test.txt  ( press enter it will create a file with name test.txt and press control C)
ctrl C to exit

now you can see a file named test will be created in client and server

MODIFY A FILE

cat >> test.txt (press enter it will go to the next line and you can type any words to modify the file)
test 1
test 2 
test 3
ctrl C ( control c to exit from file)
once this is done if you open both test file in client and server the file will be appeneded with test1 test2 test3


DELETE A FILE

type rm test.txt to remove the file both in client and server

NOW CLOSE THE NEWLY OPENED TERMINAL AS PART 3 IS DONE



-------------------------
Part 4 of the project : 
--------------------------


file name : client2.py
Clear the terminal with code:   Clear
To start the client type : python3 client2.py


it will prompt 3 items

1. Sync
2. Async
3. DeferredSync


press 1 and go along with the prompt to check sync operations
once SYNC is done 
Clear the terminal with code:   Clear
To start the client type : python3 client2.py
press 2 and go along with the prompt to check async operations
once ASYNC is done 
Clear the terminal with code:   Clear
To start the client type : python3 client2.py
press 2 and go along with the prompt to check Deferredsync operations
once DEFERREDSYNC is done 
Clear the terminal with code:   Clear






