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
        

        self.password = password
        self.method = method

    def _fernet_key(self):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=self.password.encode(), iterations=100000)
        key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
        return key

    def _fernet_encrypt(self, data):
        return Fernet(self._fernet_key()).encrypt(data)

    def _fernet_decrypt(self, data):
        return Fernet(self._fernet_key()).decrypt(data)

    def encrypt(self, data):
        if type(data) != bytes:
            raise MustBeByteLikeError("Given data must be byte-like")
        
        return self.methods[self.method][0](data)

    def decrypt(self, data):
        if type(data) != bytes:
            raise MustBeByteLikeError("Given data must be byte-like")
        
        return self.methods[self.method][1](data)
