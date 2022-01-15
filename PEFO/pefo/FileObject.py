from .Errors import *
from .Encryptor import Encryptor


class FileObject:
    def __init__(self, filename, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None, method=None, password=None):
        if not password and method:
            raise NoKeyError("You should provide key")
        elif password and not method:
            raise NoMethodError("You should provide encryption method")
        elif method and 'b' not in mode:
            raise MustBeBytesError("You should open file in binary mode for encryption")
        
        if method and password:
            self._encryptor = Encryptor(password=password, method=method)
        else:
            self._encryptor = None

        self._fileobject = open(filename, mode=mode, buffering=buffering, encoding=encoding, newline=newline, closefd=closefd, opener=opener)
        
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self._fileobject.close()

    def _decrypt(self, data):
        if not self._encryptor:
            return data
        else:
            return self._encryptor.decrypt(data)
    
    def _encrypt(self, data):
        if not self._encryptor:
            return data
        else:
            return self._encryptor.encrypt(data)

    def _mayBeNotSupported(func):
        def checker(*args, **kwargs):
            if args[0]._encryptor:
                raise NoSenceError(func.__name__)
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