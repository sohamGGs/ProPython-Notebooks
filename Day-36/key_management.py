import os
from cryptography.fernet import Fernet

def load_or_create_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return open("secret.key", "rb").read()

key = load_or_create_key()
print("Key is ready for use.")