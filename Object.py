# Noun     => Class        Eg. Animal /SuperHero
# Ajective => Attributes   Eg. Dog    /Red Cape
# Verb     => Method       Eg. Barks  /Fly

# implementation of class and object

class Employee:     #noun
    # attributes
    name = 'Ben'
    designation = 'Sales Executive'
    salesMadeThisWeek = 6
    # verb/action being performed
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek > 5:
            return 'Target Achieved!!'
        else:
            return 'Target Not Achieved!'

employeeOne = Employee()  #object for class/object instantiation
print(employeeOne.name)
print(employeeOne.hasAchievedTarget())

employeeTwo = Employee()
print(employeeTwo.name)

numbers = [1,2,3]
print(type(numbers))
numbers.append(4)
print(numbers)