## About
PEFO (Pavahali's Encrypted File Opener) is an easier way to work with encrypted files

## How it works?
This is just a wrapper for built-in function which uses fernet from [cryptography](https://pypi.org/project/cryptography/) lib

## Latest release
Project now in beta. It's stable but not all features are supported. If you already made your decision install [latest release](https://github.com/Pavahali/pefo/releases/latest/) or directly from this repo

## Todo
* Add support for unsupported methods
---
## Install

1. Clone repo and go to its directory
```
git clone https://github.com/Pavahali/pefo/
```
2. Install repo using pip
```
pip install .
```

## Quickstart
> How to encrypt data
```py
from pefo import open

with open('test.file', 'wb', password='pass') as f:
    f.write(b'Encrypted data 0_0')
```

> How to read encrypted data?
```py
from pefo import open

with open('test.file', 'rb', password='pass') as f:
    f.read()
```

> I already have key. How to use it instead of password?
```py
from pefo import open

with open('test.file', 'rb', key='your key') as f:
    f.read()
```

> Ok, but I want to use it without encryption. How I can do this?
```py
from pefo import open

with open('test.file', 'r') as f:
    f.read()
```

## Errors
`MustBeBytesError` - you should open encrypted file in binary mode

`MustBeByteLikeError` - you should write data in bytes

`NonsenceError` - action can't be done with encrypted data (actually can, but it makes no sence)

`TooManyArgs` - you can not use both key and password. Use one of them