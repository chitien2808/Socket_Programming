import psutil
import struct
import signal
import os

def killProcess(clientsocket, pid):
    try:
        os.kill(pid, signal.SIGTERM)
        clientsocket.send("kill_ok".encode())
    except:
        clientsocket.send("kill_err".encode())

def send_string_list(client_socket, string_list):
    data = '|'.join(string_list).encode('utf-8')
    # Send the total byte length first
    client_socket.sendall(len(data).to_bytes(4, 'big'))
    # Send the data
    client_socket.sendall(data)

# Iterate over all running process
def listProcess(clientsocket):
    
    all_pids = psutil.pids()
    listProcessInfo = []
    for proc in psutil.process_iter():
        try:
            # Get process details as a dictionary
            process = proc.as_dict(attrs=['pid', 'name', 'num_threads'])
            processInfo = f'{process["pid"]},{process["name"]},{process["num_threads"]}'
            listProcessInfo.append(processInfo)
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    send_string_list(clientsocket, listProcessInfo)
    print("DONE listprocess")




# if __name__ == '__main__':
#     listProcess(clie)