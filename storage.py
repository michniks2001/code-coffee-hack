import os
import json
import sys

# Ensure the package can be imported regardless of how it's run
try:
    from .encryption import encrypt, decrypt
except ImportError:
    # If running as script or the package is not installed
    package_dir = os.path.abspath(os.path.dirname(__file__))
    if package_dir not in sys.path:
        sys.path.insert(0, package_dir)
    from encryption import encrypt, decrypt

VAULT_PATH = os.path.expanduser("~/.apiport/vault.port")

def load_vault():
    if not os.path.exists(VAULT_PATH):
        return {}
    with open(VAULT_PATH, "rb") as f:
        decrypted = decrypt(f.read())
        return json.loads(decrypted)

def save_vault(data: dict):
    os.makedirs(os.path.dirname(VAULT_PATH), exist_ok=True)
    with open(VAULT_PATH, "wb") as f:
        f.write(encrypt(json.dumps(data).encode()))