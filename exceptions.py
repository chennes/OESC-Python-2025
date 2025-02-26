class OESCException(RuntimeError):
    pass

class FileFormatError(OESCException):
    def __init__(self, filename:str):
        self.filename = filename

class InvalidIdError(OESCException):
    """Raised when an employee ID does not meet requirements"""
    def __init__(self, id:str):
        self.id = id

class BadHoursError(OESCException):
    """ Raised when we get a number of hours available that is not
    valid (less than zero or more than the number of hours in a week,
    or not a number at all)."""
    def __init__(self, hours):
        self.hours = hours

class InvalidNameError(OESCException):
    """Raised on an invalid human name, like someone without a first name"""