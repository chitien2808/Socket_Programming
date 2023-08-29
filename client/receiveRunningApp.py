from GUI import communicate
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "GUI\\tempData\\apprunningData.txt") 

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

    
def receiveRunningApp(clientsocket):
    data = receive_string_list(clientsocket)
    with open(file_path, "w", encoding='utf-8') as fo:
        for val in data:
            fo.writelines(val + '\n')
    communicate.queue_to_main.put("displayrunningapp")
    print("DONE")

def receiveStatus(clientsocket):
    communicate.status = clientsocket.recv(1024).decode()
    communicate.queue_to_main.put(communicate.status + "_app") 
    print(communicate.status)
