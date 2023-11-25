from abc import ABC, abstractmethod
from cryptography.fernet import Fernet


class Cryptutil():


    # Generating the key and writing it to a file
    def genwrite_key(self):
        key = Fernet.generate_key()
        with open("pass.key", "wb") as key_file:
            key_file.write(key)

    # Function to load the key
    def call_key(self):
        return open("pass.key", "rb").read()

    def encrypt(self, value: str) -> str:
        key = self.call_key()
        slogan = value.encode()
        a = Fernet(key)
        coded_slogan = a.encrypt(slogan)
        print("coded_slogan = ", coded_slogan)
        return coded_slogan


    def decrypt(self, value: str) -> str:
        key = self.call_key()
        b = Fernet(key)
        decoded_slogan = b.decrypt(value)
        print("decoded_slogan = ", decoded_slogan)
        return decoded_slogan