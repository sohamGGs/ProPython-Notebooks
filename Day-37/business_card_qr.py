import qrcode

def generate_vcard_qr(name, email, github):
    vcard = f"BEGIN:VCARD\nVERSION:3.0\nN:{name}\nEMAIL:{email}\nURL:{github}\nEND:VCARD"
    qr = qrcode.QRCode(box_size=15, border=2)
    qr.add_data(vcard)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="#1a73e8", back_color="white")
    img.save("soham_contact_qr.png")
    print("VCard QR saved as 'soham_contact_qr.png'")

if __name__ == "__main__":
    generate_vcard_qr("Soham Patil", "soham@example.com", "https://github.com/soham")