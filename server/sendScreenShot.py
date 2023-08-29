from PIL import ImageGrab
import struct
import io


def sendScreenShot(clientSocket):
    print("loading..")
    screenshot = ImageGrab.grab()
    screenshot_bytes = io.BytesIO()
    screenshot.save(screenshot_bytes, format='PNG')
    screenshot_bytes = screenshot_bytes.getvalue()

    # Send the size of the image data first
    size = len(screenshot_bytes)
    clientSocket.sendall(struct.pack('!I', size))
    # Then send the image data
    clientSocket.sendall(screenshot_bytes)

    print("Screenshot sent successfully")
