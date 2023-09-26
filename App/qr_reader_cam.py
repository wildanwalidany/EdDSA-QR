import pyzbar.pyzbar as pyzbar
import cv2

class Reader:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)  # Initialize the camera (0 for default camera)
        self.data = None

    def read(self):
        while True:
            ret, frame = self.cap.read()  # Read a frame from the camera
            if not ret:
                break

            # Decode QR codes in the frame
            decoded_objs = pyzbar.decode(frame)

            if decoded_objs:
                self.data = decoded_objs[0].data.decode('utf-8')  # Assuming there's only one QR code
                break  # Stop processing frames after finding a QR code

        self.cap.release()  # Release the camera
        return self.data

# Example usage
if __name__ == "__main__":
    qr_reader = Reader()
    qr_data = qr_reader.read()

    if qr_data is not None:
        print("QR Code Data:", qr_data)
    else:
        print("QR code reading failed.")
