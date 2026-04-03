import qrcode

try:
    qr = qrcode.QRCode(version=1) # Version 1 is small
    long_text = "A" * 2000 # Too much for version 1
    qr.add_data(long_text)
    qr.make(fit=False) # Fit=False forces it to fail if data is too big
except qrcode.exceptions.DataOverflowError:
    print("Error: Data is too large for this QR version!")