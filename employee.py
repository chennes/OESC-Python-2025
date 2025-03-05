from typing import Optional
from exceptions import InvalidIdError, BadHoursError, InvalidNameError

def is_valid_id(id:str) -> bool:
    """Check if an ID meets our requirements:
    1) Must be a 6-digit non-negative integer
    2) Cannot be 000000 or 999999"""
    try:
        id_as_int = int(id)
        if len(id) != 6:
            return False
        if id_as_int == 0 or id_as_int == 999999:
            return False
        if id_as_int < 0:
            return False
    except ValueError:
        return False
    return True

def is_ascii_alpha(data:str) -> bool:
    for c in data.upper():
        if ord(c) < 65 or ord(c) > 90:
            return False
    return True

class Employee:
    def __init__(self, id:str, last_name:str, first_name:str, middle_name:Optional[str] = None):
        if not is_valid_id(id):
            raise InvalidIdError(id)
        self._id = id
        self.set_name(last_name, first_name, middle_name)
        self._available_hours = None

    def __repr__(self) -> str:
        ret_value = f"{self._last_name}, {self._first_name}"
        if self._middle_name:
            ret_value += f" {self._middle_name}"
        ret_value += f" [{self._id}]"
        if self._available_hours is not None:
            ret_value += f" [{self._available_hours} available hours]"
        else:
            ret_value += f" [Available hours has not been set]"
        return ret_value
    
    def set_name(self, last_name:Optional[str] = None, first_name:Optional[str] = None, middle_name:Optional[str] = None):
        """Validate input and store new name. Middle name is optional."""
        if last_name is not None:
            self._last_name = last_name
        if first_name is not None:
            if first_name == "":
                raise InvalidNameError()
            self._first_name = first_name
        if middle_name is not None:
            self._middle_name = middle_name
    
    def set_available_hours(self, num_hours:int):
        try:
            if not isinstance(num_hours, int):
                raise BadHoursError(num_hours)
            as_int = int(num_hours)
            if as_int < 0:
                raise BadHoursError(num_hours)
            if as_int > 7*24+1:
                raise BadHoursError(num_hours)
            self._available_hours = num_hours
        except ValueError as exception:
            raise BadHoursError(num_hours) from exception
        
    def get_available_hours(self):
        return self._available_hours
