# instance methods

class Employee:
    def employeeDetails(self):
        self.name = "Ben"

    def welcomeMessage():
        return ("Welcome to org")

employee = Employee()
employee.employeeDetails()
print(employee.name)
# employee.welcomeMessage()
# print(employee.welcomeMessage())  # wont work as self is not present in method

# to overcome the above problem we use static method
# static method is a decotor as makes use understand it as static method

class Employee:
    def employeeDetails(self):
        self.name = "Ben2"

    @staticmethod
    def welcomeMessage():
        return ("Welcome to org2")

employee = Employee()
employee.employeeDetails()
print(employee.name)
print(employee.welcomeMessage())



