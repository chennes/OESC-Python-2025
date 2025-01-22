#import zoo
from employee import Employee

# make sure this is the main entry before starting the zoo
if __name__ == "__main__":
    #the_zoo = zoo.Zoo()
    my_employee = Employee(id="123456", last_name="Smith", first_name="Jane", middle_name="'Awesome'")
    my_employee.set_name(last_name="Smith")
    my_employee.set_available_hours("thing that is not an int")
    print(my_employee)
    