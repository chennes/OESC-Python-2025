from exceptions import FileFormatError
import os
import datetime

class Zoo:

    def __init__(self):
        self.employees = []
        self.load_employee_information()

    def load_employee_information(self):
        """Loads the file employees.csv and stores in a member list"""
        try:
            last_mod_timestamp = os.path.getmtime("employees.csv")
            last_mod_date = datetime.datetime.fromtimestamp(last_mod_timestamp)
            today = datetime.datetime.now()
            time_diff = today - last_mod_date
            if time_diff.days > 1:
                pass
                #raise FileTooOldError()
            with open("employees.csv","r",encoding="utf-8") as f:
                line = f.readline()
                if line.find("name") == -1:
                    raise FileFormatError("employees.csv")
                while(line):
                    line = f.readline()
                    employee_data = line.split(",")
                    if len(employee_data) == 4:
                        employee = {
                            "last":employee_data[0],
                            "first":employee_data[1],
                            "middle":employee_data[2],
                            "hours":int(employee_data[3])
                        }
                        self.employees.append(employee)
        except FileNotFoundError as err:
            print("You forgot to make the employees.csv file")
            print(err)