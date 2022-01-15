## About
PEFO (Pavahali's Encrypted File Opener) is an easier way to work with encrypted files in python.

## How does it work?
This is just a wrapper for built-in function which uses [cryptography](https://pypi.org/project/cryptography/) lib for encryption

## Latest release
Project now in alpha so I don't recommend you to use it now. It's stable but not all features are supported. But if you already made your decision here is a link for you: https://github.com/Pavahali/pefo/releases/latest/

## Todo
* Add other encryption algorithms (AES, Camellia, etc.)
* Add support for unsupported methods

---
## Install
Get one of [pefo releases](https://github.com/Pavahali/pefo/releases) (either .whl or .tar.gz archive) and use pip to install it:
```
pip install file
```

## Quickstart
Encrypt data with fernet
```py
from pefo import open

with open('test.file', 'wb', method='fernet', password='pass') as f:
    f.write(b'Encrypted data 0_0')
```

Read encrypted data with fernet

```py
from pefo import open

with open('test.file', 'rb', method='fernet', password='pass') as f:
    f.read()
```

Just read normal file

```py
from pefo import open

with open('test.file', 'r') as f:
    f.read()
```

## Errors
`InvalidMethodError` - method you provided does not exist or not supported

`MustBeBytesError` - you should open encrypted file in binary mode

`MustBeByteLikeError` - you should write data in bytes

`NoPassError` - if you provided method you must give password

`NoMethodError` - if you provided password you must give method

`NoSenceError` - action can't be done with encrypted data (actually can, but it makes no sence)

---

## Else
My [discord server](https://discord.gg/SuzJ7UamMG) where you can get help with this library
