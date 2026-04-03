import qrcode

# Simple QR
img = qrcode.make("https://github.com/SohamPatil")
img.save("my_github_qr.png")
print("Basic QR Generated.")