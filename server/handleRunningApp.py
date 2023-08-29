import psutil
import signal
import sys
import os
from io import StringIO
from pywinauto import Desktop
from AppOpener import open


def openApp(clientsocket, appName):
    original_stdout = sys.stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    open(appName)
    # Reset the stdout back to original and get the message
    sys.stdout = original_stdout
    message = captured_output.getvalue().strip()

    if "not found" in message.lower():
        clientsocket.send("open_err".encode()) 
    else:
        clientsocket.send("open_ok".encode())




def killRunningApp(clientsocket, pid):
    try:
        os.kill(pid, signal.SIGTERM)
        clientsocket.send("kill_ok".encode())
    except:
        clientsocket.send("kill_err".encode())
    
    # Sending a response to the client about the result
    # listRunningApp(clientsocket)

def checkValidApp(w):
    try:
        full_title = w.window_text()
        if full_title == "Taskbar" or full_title == "": return False
        proc_id = w.process_id()
        process = psutil.Process(proc_id)
        thread_count = process.num_threads()
    except psutil.NoSuchProcess:
        return False 
    if ' - ' in full_title:
        app_name = full_title.rsplit(' - ', 1)[1]
    else:
        app_name = full_title
    return f'{proc_id},{app_name},{thread_count}'


def send_string_list(client_socket, string_list):
    data = '|'.join(string_list).encode('utf-8')
    # Send the total byte length first
    client_socket.sendall(len(data).to_bytes(4, 'big'))
    # Send the data
    client_socket.sendall(data)


def listRunningApp(clientsocket):
    windows = Desktop(backend="uia").windows()
    runningApp = []
    for w in windows:
        tmp = checkValidApp(w)
        if (tmp == False) : continue 
        runningApp.append(tmp)
    send_string_list(clientsocket, runningApp)
    print("DONE")
