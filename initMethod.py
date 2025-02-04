class Employee:
    def __init__(self, name):
        self.name = name

    # def employeeDetails(self):
    #     self.name = 'Mark'

    def displayEmployeeDetails(self):
        print(self.name)    # instance attribute

employee = Employee("Mark")
employeeTwo = Employee("Mathew")
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()