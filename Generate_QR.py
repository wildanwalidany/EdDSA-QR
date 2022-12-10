import qrcode

# Create a new QR code object
qr = qrcode.QRCode()

# Set the data for the QR code
qr.add_data("Wildan Dharma Walidany")

# Generate the QR code
qr.make()

# Create an image of the QR code
img = qr.make_image()

# Save the image to a file
img.save("qr_code.png")