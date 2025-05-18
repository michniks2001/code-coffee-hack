from cryptography.fernet import Fernet
import os

KEY_PATH = os.path.expanduser("~/.apiport_key")

def get_key():
    if os.path.exists(KEY_PATH):
        with open(KEY_PATH, "rb") as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as f:
            f.write(key)
        return key

def encrypt(data: bytes) -> bytes:
    return Fernet(get_key()).encrypt(data)

def decrypt(data: bytes) -> bytes:
    return Fernet(get_key()).decrypt(data)
