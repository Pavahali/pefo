class NoSenceError(Exception):
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

class InvalidMethodError(Exception):
    """
    If user provided not existing method
    """
    def __init__(self, method):
        self.method = method
        
    def __str__(self):
        return f"Method '{self.method}' does not exist"

class MustBeByteLikeError(Exception):
    """
    If given data are not bytes-like object
    """
    pass

class NoKeyError(Exception):
    """
    If user provided encryption method and does not gave password
    """
    pass

class NoMethodError(Exception):
    """
    If user provided password but does not gave encryption method
    """
    pass