import qrcode

class QREncode:
    def __init__(self, encoded_signature):
        # Generate a QR code from the encoded signature
        self.qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        self.qr.add_data(encoded_signature)
        self.qr.make(fit=True)

        # Save the QR code as an image
        self.img = self.qr.make_image(fill_color="black", back_color="white")
        self.img.save("./App/qrcode.png")

        return None