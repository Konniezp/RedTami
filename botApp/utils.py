from cryptography.fernet import Fernet
from django.conf import settings

cipher_suite = Fernet(settings.ENCRYPT_KEY)

def encrypt_data(data):
    """Cifra datos sensibles y retorna bytes."""
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data):
    """Descifra datos y retorna string en texto plano."""
    return cipher_suite.decrypt(encrypted_data).decode()
