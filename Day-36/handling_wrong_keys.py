from cryptography.fernet import Fernet, InvalidToken

key1 = Fernet.generate_key()
key2 = Fernet.generate_key()

cipher = Fernet(key1)
token = cipher.encrypt(b"Sensitive Data")

try:
    # Trying to decrypt with the wrong key
    wrong_cipher = Fernet(key2)
    wrong_cipher.decrypt(token)
except InvalidToken:
    print("Security Alert: Decryption failed! Wrong key used.")