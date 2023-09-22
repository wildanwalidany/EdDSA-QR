import pyzbar.pyzbar as pyzbar
import cv2

class Reader():
    def __init__(self):
        
        # Read the image
        image = cv2.imread("App/qrcode.png")

        # Decode the QR code
        decoded_objs = pyzbar.decode(image)

        # Store decoded_objs into data
        for obj in decoded_objs:
            self.data = obj.data

    def read(self):

        return self.data



