class Employee:
    def employeeDetails(self):
        self.name = 'John'
        print("Name: ",self.name)
        self.age = 30
        print("Age: ",self.age)
    def printEmployeeDetails(self):
        print("Printing in another method")
        print("Name: ",self.name)
        print("Age: ", self.age) # age cant be used if self is not mentioned

employee = Employee()
employee.employeeDetails()
employee.printEmployeeDetails()
# Employee.employeeDetails(employee)


