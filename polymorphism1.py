class Employee:
    def setNumberWorkingHrs(self):
        self.numberofWorkingHours = 40

    def displayWorkingHours(self):
        print(self.numberofWorkingHours)

class Trainee(Employee):        #polymorphism
    def setNumberWorkingHrs(self):
        self.numberofWorkingHours = 45

    def resetNumberofHours(self):
        super().setNumberWorkingHrs()

employee = Employee()
employee.setNumberWorkingHrs()
print("number of working of employee ", end=" ")
employee.displayWorkingHours()

trainee = Trainee()
trainee.setNumberWorkingHrs()
print("number of working of trainee ", end=" ")
trainee.displayWorkingHours()

trainee.setNumberWorkingHrs()
print("number of working of trainee after reset ", end=" ")
trainee.displayWorkingHours()