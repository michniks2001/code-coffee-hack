
from .storage import load_vault, save_vault
import os

def add(secret_name, secret_value):
    vault = load_vault()
    vault[secret_name] = secret_value
    save_vault(vault)
    print(f"[+] Added secret: {secret_name}")

def delete(secret_name):
    vault = load_vault()
    if secret_name in vault:
        del vault[secret_name]
        save_vault(vault)
        print(f"[x] Deleted secret: {secret_name}")
    else:
        print("[!] Secret not found")

def update(secret_name, new_value):
    vault = load_vault()
    if secret_name in vault:
        vault[secret_name] = new_value
        save_vault(vault)
        print(f"[~] Updated secret: {secret_name}")
    else:
        print("[!] Secret not found")

def list_secrets():
    vault = load_vault()
    if not vault:
        print("[*] No secrets stored.")
    else:
        print("[*] Stored secrets:")
        for key in vault:
            print(f" - {key}")

def import_to_env(secret_name):
    vault = load_vault()
    if secret_name in vault:
        with open(".env", "a") as f:
            f.write(f"{secret_name}={vault[secret_name]}\n")
        print(f"[+] Imported {secret_name} to .env")
    else:
        print("[!] Secret not found")
