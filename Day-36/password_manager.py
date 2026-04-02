import json
import os
from cryptography.fernet import Fernet

class PassVault:
    def __init__(self):
        self.key = self._get_key()
        self.cipher = Fernet(self.key)
        self.file = "vault.json"

    def _get_key(self):
        if not os.path.exists("vault.key"):
            key = Fernet.generate_key()
            with open("vault.key", "wb") as f: f.write(key)
        return open("vault.key", "rb").read()

    def add_password(self, site, password):
        encrypted = self.cipher.encrypt(password.encode()).decode()
        data = self._load_vault()
        data[site] = encrypted
        with open(self.file, "w") as f: json.dump(data, f)

    def _load_vault(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f: return json.load(f)
        return {}

if __name__ == "__main__":
    vault = PassVault()
    vault.add_password("Github", "SohamPass2026")
    print("Password stored securely.")