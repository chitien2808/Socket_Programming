from tkinter import filedialog
from tkinter import Tk
from PIL import Image 
from GUI import communicate
import struct
import io
import os 
script_dir = os.path.dirname(__file__)
tempImage_path = os.path.join(script_dir, "GUI/tempData/tempImage.png")

def saveImage():
    root = Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    
    if file_path:  # If a file path is provided
        img = Image.open(tempImage_path)
        img.save(file_path)
        print(f"Screenshot saved to {file_path}")
    else:
        print("Screenshot not saved")

    
def readImage(client_socket):
    # First read the size of the image data
    size = struct.unpack('!I', client_socket.recv(4))[0]
    received_data = b''
    while len(received_data) < size:
         data = client_socket.recv(1024)
         received_data += data

    img = Image.open(io.BytesIO(received_data))
    img.save(tempImage_path)
    print("Screenshot received successfully and loaded into PIL.Image object")
    communicate.queue_to_main.put("displayimage")
    # menuScreen.displayImage(communicate.src_screen)
    # img.show()
    # save = input("save?")
    # if (save == "y") : saveImage(img)
