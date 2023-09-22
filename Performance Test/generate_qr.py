import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(filename)
    
    n = qr.version
    k = qr.version - qr.error_correction - 1
    
    print(f"QR code saved as: {filename}")
    print(f"n: {n}")
    print(f"k: {k}")

# Example usage
data = "ICE-BEAR"
filename = "qrcode.png"
generate_qr_code(data, filename)
