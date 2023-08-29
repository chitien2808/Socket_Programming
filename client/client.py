import socket
import receiveScreenShot
import receiveRunningApp
import receiveProcess
import threading
from GUI import communicate
from GUI import menuScreen
from receiveKeyLogger import *


def valid(command):
    return not(command in communicate.blackListCommand)

def start_client():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = '192.168.2.100'
    # print(communicate.ipHost)
    host = communicate.ipHost if communicate.ipHost else 'localhost'
    print(host)
    port = 11137
    try:
        clientsocket.connect((host, port))
        communicate.status_connection = 2
        print("Connection succesful")
    except:
        print("Failed to connect")
        clientsocket.close()
        communicate.init()
        return False
    try:
        while True:
            # command = input("Enter message to send to server: ")
            while True:
                if communicate.command != '' : 
                    command = communicate.command
                    break
            if valid(command) : clientsocket.send(command.encode('ascii'))
            command = list(map(str, command.split()))
            flag = command[0]
            
            if flag == "screenshot": receiveScreenShot.readImage(clientsocket)
            elif flag == "saveimage": receiveScreenShot.saveImage()
            elif flag == "listprocess": receiveProcess.receiveProcess(clientsocket)
            elif flag == "killprocess": receiveProcess.receiveStatus(clientsocket)
            elif flag == "listrunningapp": receiveRunningApp.receiveRunningApp(clientsocket)
            elif flag == "killrunningapp": receiveRunningApp.receiveStatus(clientsocket)
            elif flag == "openapp": receiveRunningApp.receiveStatus(clientsocket)
            elif flag == "hook" or flag == "unhook": pass #chua
            elif flag == "sendkeylogger": receiveKeylogger(clientsocket) #chua
            elif flag == "disconnect":
                clientsocket.close()
                communicate.init()
                return False
            elif flag == "shutdown": break
            else:
                data = clientsocket.recv(1024)
                print('Received from server: ', data.decode('ascii'))
            if flag == 'QUIT': break
            communicate.command = ''
    except:
        clientsocket.close()
        communicate.init()
        return False
    clientsocket.close()
    communicate.init()
    return True

def run_client():
    while (communicate.command != "QUIT") and (communicate.status_connection != 1 or not(start_client())): pass

if __name__ == "__main__":
    backend_thread = threading.Thread(target=run_client)
    backend_thread.start()
    menuScreen.run_GUI()
    
    # start_client()
