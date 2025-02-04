# access specifier

# public, private, protected

# Public => memberName
# Protected => _memberName
# Private => __memberName

class Car:
    numberOfWheels = 4
    _color = "black"
    __year = 2017  # _Car__year
class BMW(Car):
    def __init__(self):
        print("Protected Attibute ", self._color)

car = Car()
print("Public attribute ", car.numberOfWheels)
bmw = BMW()
print("Private attribute ", car._Car__year)
