from cryptography.fernet import Fernet

# Generate a key (Save this! If lost, you can't decrypt)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypting
text = b"MySecretPassword123"
encrypted_text = cipher_suite.encrypt(text)
print(f"Encrypted: {encrypted_text}")

# Decrypting
decrypted_text = cipher_suite.decrypt(encrypted_text)
print(f"Decrypted: {decrypted_text.decode()}")