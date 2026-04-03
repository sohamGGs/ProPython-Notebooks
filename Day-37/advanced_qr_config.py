import qrcode

qr = qrcode.QRCode(
    version=1, # Size (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("Welcome to Day 37")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("styled_qr.png")