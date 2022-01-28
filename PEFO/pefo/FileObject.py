from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from .Errors import *
import base64


class FileObject:
    def __init__(self, filename: str, mode: str = 'r', buffering: int = -1, encoding: str = None, errors: str = None, newline: str = None, closefd: bool = True, opener = None, key: str = None, password: str = None):
        if key and password:
            raise TooManyArgs("You should provide either password or key")
        if key or password:
            self._encrypted = True

            if key:
                self.key = key
            else:
                self.key = base64.urlsafe_b64encode(self._keygen(password.encode()))

        self._fileobject = open(filename, mode=mode, buffering=buffering, encoding=encoding, newline=newline, closefd=closefd, opener=opener)
        
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self._fileobject.close()

    def _keygen(self, source: bytes):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=source, iterations=100000)
        return kdf.derive(source)

    def _decrypt(self, data):
        if not self._encrypted:
            return data
        
        if type(data) != bytes:
            raise MustBeByteLikeError("Given data must be byte-like")
        
        return Fernet(self.key).decrypt(data)
    
    def _encrypt(self, data):
        if not self._encrypted:
            return data

        if type(data) != bytes:
            raise MustBeByteLikeError("Given data must be byte-like")
        
        return Fernet(self.key).encrypt(data)

    def _mayBeNotSupported(func):
        def checker(*args, **kwargs):
            if args[0]._encryptor:
                raise NonsenceError(func.__name__)
            return func(*args, **kwargs)
        return checker

    def close(self):
        self._fileobject.close()

    def fileno(self):
        return self._fileobject.fileno()
    
    def flush(self):
        self._fileobject.flush()
    
    def isatty(self):
        return self._fileobject.isatty()
    
    def read(self, size=-1):
        return self._decrypt(self._fileobject.read(size))

    def readable(self):
        return self._fileobject.readable()
    
    @_mayBeNotSupported
    def readline(self, size=-1):
        return self._fileobject.readline(size)
    
    @_mayBeNotSupported
    def readlines(self, hint=-1):
        return self._fileobject.readlines(hint)
    
    def seek(self, offset):
        self._fileobject.seek(offset)
    
    def seekable(self):
        return self._fileobject.seekable()
    
    def tell(self):
        return self._fileobject.tell()
    
    @_mayBeNotSupported
    def truncate(self, size=None):
        return self._fileobject.truncate(size)

    def writable(self):
        return self._fileobject.writable()
    
    def write(self, byte):
        self._fileobject.write(self._encrypt(byte))
    
    def writelines(byte):
        self._fileobject.write(self._encrypt(''.join(byte)))


# All Errors
class NonsenceError(Exception):
    """
    If action makes no sence (with encrypted data)
    """
    def __init__(self, action):
        self.action = action
        
    def __str__(self):
        return f"Used function ('{self.action}') does not supported while working with encrypted data"

class MustBeBytesError(Exception):
    """
    If encrypted file opened without binary mode
    """
    pass

class MustBeByteLikeError(Exception):
    """
    If given data are not bytes-like object
    """
    pass

class TooManyArgs(Exception):
    """
    If user gives both key and password
    """