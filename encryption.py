from cryptography.fernet import Fernet

KEY_FILE = "key.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

def get_fernet():
    return Fernet(load_key())

def encrypt_password(password):
    return get_fernet().encrypt(password.encode()).decode()

def decrypt_password(encrypted):
    return get_fernet().decrypt(encrypted.encode()).decode()
