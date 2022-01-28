from setuptools import setup, find_packages

VERSION = '0.1' 
DESCRIPTION = "Pavahali's Encrypted File Opener"
LONG_DESCRIPTION = 'An easier way to work with encrypted files'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="pefo", 
        version=VERSION,
        author="Pavahali",
        author_email="<pavahalis@protonmail.ch>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        url='https://github.com/Pavahali/pefo/',
        install_requires=['cryptography'],
        keywords=['pavahali', 'file', 'open', 'cryptography', 'encryption'],
        classifiers= [
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux"
        ]
)
