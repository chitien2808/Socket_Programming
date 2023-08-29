from GUI import communicate
import struct
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "GUI\\tempData\\processData.txt") 

def receive_string_list(clientsocket):
    # First, receive the total byte-length
    data_length = int.from_bytes(clientsocket.recv(4), 'big')

    chunks = []
    bytes_received = 0

    while bytes_received < data_length:
        chunk = clientsocket.recv(min(data_length - bytes_received, 4096))
        if not chunk:
            raise ConnectionError("Connection lost before receiving all data")
        
        chunks.append(chunk)
        bytes_received += len(chunk)

    data = b''.join(chunks).decode('utf-8')
    return data.split('|')

def receiveProcess(clientsocket):
    processInfo = receive_string_list(clientsocket)
    with open(file_path, 'w') as fo:
        for pcInfo in processInfo:
            fo.writelines(pcInfo + '\n')
    communicate.queue_to_main.put("displayprocess")
    print("DONE listprocess")

def receiveStatus(clientsocket):
    communicate.status = clientsocket.recv(1024).decode()
    communicate.queue_to_main.put(communicate.status + "_process")
