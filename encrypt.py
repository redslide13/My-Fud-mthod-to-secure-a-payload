from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def aes_encrypt(input_file, output_file, key):

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    with open(input_file, 'rb') as f_input:
        plaintext = f_input.read()


    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()


    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    with open(output_file, 'wb') as f_output:
        f_output.write(iv + ciphertext)

def generate_key():
    return os.urandom(32)

if __name__ == "__main__":
    key = generate_key()
    input_file = 'input.exe'
    output_file = 'output.bin'
    aes_encrypt(input_file, output_file, key)
    print("Datei erfolgreich verschlüsselt!","\nmit dem key:", key)
