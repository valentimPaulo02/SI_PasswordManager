from cryptography.fernet import Fernet
import base64, os

def encrypt_password(password):
    key_bytes = get_key().encode()
    fernet = Fernet(key_bytes)

    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password.decode()

def decrypt_password(encrypted_password):
    key_bytes = get_key().encode()
    fernet = Fernet(key_bytes)

    decrypted_password = fernet.decrypt(encrypted_password.encode())
    return decrypted_password.decode()

def get_key():
    key_hex = os.environ['KEY'] # -------------------------- ENV VARIABLE
    key_bytes = bytes.fromhex(key_hex)
    key_base64 = base64.urlsafe_b64encode(key_bytes).decode()
    return key_base64