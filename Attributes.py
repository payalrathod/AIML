# attributes and methods

class Employee:
    numberofWorkingHours = 40

# class attributes
employeOne = Employee()
employeTwo = Employee()
print(employeOne.numberofWorkingHours)
print(employeTwo.numberofWorkingHours)

Employee.numberofWorkingHours = 45
print(employeOne.numberofWorkingHours)
print(employeTwo.numberofWorkingHours)

# instance attributes
employeOne.name = 'John'
# attribute created only for employeeOne
print(employeOne.name)

employeTwo.name = 'Mary'
print(employeTwo.name)

employeOne.numberofWorkingHours = 40
print(employeOne.numberofWorkingHours) #only specific to attribute

print(employeTwo.numberofWorkingHours)


