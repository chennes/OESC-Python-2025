class OESCException(RuntimeError):
    pass

class FileFormatError(OESCException):
    def __init__(self, filename:str):
        self.filename = filename

class InvalidIdError(OESCException):
    """Raised when an employee ID does not meet requirements"""
    def __init__(self, id:str):
        self.id = id
