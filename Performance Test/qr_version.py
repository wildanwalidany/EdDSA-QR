import pyzbar.pyzbar as pyzbar
from PIL import Image

class QRCodeVersionChecker:
    def __init__(self, qr_code_image_path):
        self.qr_code_image_path = qr_code_image_path

    def get_version(self):
        image = Image.open(self.qr_code_image_path)
        decoded_objs = pyzbar.decode(image)
        if decoded_objs:
            qr_code_data = decoded_objs[0].data.decode('utf-8')
            metadata = qr_code_data.split(';')
            for item in metadata:
                if item.startswith("VER:"):
                    version = item.split(":")[1]
                    return version
        return None

# Usage example
image_path = "./App/qrcode.png"
version_checker = QRCodeVersionChecker(image_path)
qr_code_version = version_checker.get_version()
if qr_code_version:
    print("QR Code Version:", qr_code_version)
else:
    print("No QR code found in the image.")
