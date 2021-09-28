from cryptography.fernet import Fernet  



class Encryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt(self, message):
        encrypted = self.fernet.encrypt(message.encode())
        return encrypted
    
    def decrypt(self, encrypted):
        decrypted = self.fernet.decrypt(encrypted)
        return decrypted
