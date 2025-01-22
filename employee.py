from typing import Optional
from exceptions import InvalidIdError

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


class Employee:
    def __init__(self, id:str, last_name:str, first_name:str, middle_name:Optional[str] = None):
        if not is_valid_id(id):
            raise InvalidIdError(id)
        self._id = id
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    def __repr__(self) -> str:
        ret_value = f"{self._last_name}, {self._first_name}"
        if self._middle_name:
            ret_value += f" {self._middle_name}"
        ret_value += f" [{self._id}]"
        return ret_value
    
