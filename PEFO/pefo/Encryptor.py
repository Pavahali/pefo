from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from .Errors import *
import base64
import os

class Encryptor:
    def __init__(self, password: str, method: str):
        self.methods = { # other methods will be there soon
            "fernet": [self._fernet_encrypt, self._fernet_decrypt]
            }

        if method not in self.methods.keys():
            raise InvalidMethodError(method)        
        
        if method == 'fernet':
            self.key = base64.urlsafe_b64encode(self._keygen(password, 32))
        self.method = method
    
    def _keygen(self, source: str, lenth: int):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=source.encode(), iterations=100000)
        return kdf.derive(source.encode())

    def _fernet_encrypt(self, data):
        return Fernet(self.key).encrypt(data)

    def _fernet_decrypt(self, data):
        return Fernet(self.key).decrypt(data)
    
    def _aes_encrypt(self, data):
        pass
    
    def _aes_decrypt(self, data):
        pass

    def encrypt(self, data):
        if type(data) != bytes:
            raise MustBeByteLikeError("Given data must be byte-like")
        
        return self.methods[self.method][0](data)

    def decrypt(self, data):
        if type(data) != bytes:
            raise MustBeByteLikeError("Given data must be byte-like")
        
        return self.methods[self.method][1](data)
