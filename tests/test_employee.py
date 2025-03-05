import unittest
import unittest.mock

import exceptions
import employee
#from employee import Employee

class TestUtilityFunctions(unittest.TestCase):

    def test_is_valid_id_not_all_zeros(self):
        result = employee.is_valid_id("000000")
        self.assertFalse(result)

    def test_is_valid_id_not_all_nines(self):
        result = employee.is_valid_id("999999")
        self.assertFalse(result)

    def test_is_valid_id_not_letters(self):
        result = employee.is_valid_id("ABCDEFG")
        self.assertFalse(result)

    def test_is_valid_id_bad_ids_caught(self):
        bad_inputs = [
            "🔥🔥🔥🔥🔥🔥",
            "123🔥56",
            "🔥2345",
            "\x002345",
            "\x072345"
        ]
        for inp in bad_inputs:
            self.assertFalse(employee.is_valid_id(inp))

    def test_is_valid_id_not_more_than_six_chars(self):
        result = employee.is_valid_id("1234567")
        self.assertFalse(result)

    def test_is_valid_id_not_less_than_six_chars(self):
        result = employee.is_valid_id("12345")
        self.assertFalse(result)

    def test_is_valid_id_not_negative(self):
        result = employee.is_valid_id("-12345")
        self.assertFalse(result)

    def test_is_valid_id_for_valid_id(self):
        result = employee.is_valid_id("123456")
        self.assertTrue(result)

    def test_is_ascii_alpha_good_data(self):
        result = employee.is_ascii_alpha("ABCDEFG")
        self.assertTrue(result)

    def test_is_ascii_alpha_lowercase(self):
        result = employee.is_ascii_alpha("abcdefghijklmnopqrstuvwxyz")
        self.assertTrue(result)
        
    def test_is_ascii_alpha_numbers(self):
        result = employee.is_ascii_alpha("123456")
        self.assertFalse(result)


class TestEmployee(unittest.TestCase):
    
    def test_create_employee_with_invalid_id(self):
        with self.assertRaises(exceptions.InvalidIdError):
            with unittest.mock.patch("employee.is_valid_id") as mock_id_checker:
                mock_id_checker.return_value = False
                test_employee = employee.Employee("123456", "Doe", "John")

    def test_create_employee_with_no_first_name(self):
        with self.assertRaises(exceptions.InvalidNameError):
            employee.Employee("123456", "Doe", "")

    def test_create_employee_with_no_last_name(self):
        new_employee = employee.Employee("123456", "", "John")
        self.assertEqual(new_employee._first_name, "John")

    def test_create_employee_with_middle_name(self):
        new_employee = employee.Employee("123456", "Doe", "John", "Q.")
        self.assertEqual(new_employee._middle_name, "Q.")

    def test_set_available_hours_normal_hours(self):
        new_employee = employee.Employee("123456", "Doe", "John")
        new_employee.set_available_hours(40)

    def test_set_available_hours_too_big(self):
        new_employee = employee.Employee("123456", "Doe", "John")
        with self.assertRaises(exceptions.BadHoursError):
            new_employee.set_available_hours(24*7+2)

    def test_set_available_hours_too_small(self):
        new_employee = employee.Employee("123456", "Doe", "John")
        with self.assertRaises(exceptions.BadHoursError):
            new_employee.set_available_hours(-1)

    def test_set_available_hours_non_number(self):
        new_employee = employee.Employee("123456", "Doe", "John")
        with self.assertRaises(exceptions.BadHoursError):
            new_employee.set_available_hours("Forty two")

    def test_set_available_hours_non_int(self):
        new_employee = employee.Employee("123456", "Doe", "John")
        with self.assertRaises(exceptions.BadHoursError):
            new_employee.set_available_hours(12.345)

    def test_get_available_hours_init_condition(self):
        new_employee = employee.Employee("123456", "Doe", "John")
        hours = new_employee.get_available_hours()
        self.assertIsNone(hours)

    def test_get_available_hours_after_set(self):
        new_employee = employee.Employee("123456", "Doe", "John")
        new_employee.set_available_hours(40)
        hours = new_employee.get_available_hours()
        self.assertEqual(hours, 40)


