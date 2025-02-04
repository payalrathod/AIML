# magic methods
class Car():
    def __new__(self, window, door, enginetype):
        print("object initilization started")
    def __init__(self, window, door, enginetype):  # initialization constructor
        self.window = window
        self.door = door
        self.enginetype = enginetype

    def __str__(self):  # override functionality
        return 'object initialised'
        # print("object initialized") TypeError: __str__ returned non-string (type NoneType)

    def __sizeof__(self):
        return 'overall size'

    def drive(self):  # method in class
        print("person drives car")



c = Car(4, 5, 'petrol')  # object created
print(c)
print(dir(c))  # magic methods
print(c.__sizeof__())


'''
class Car():
    def __init__(self, window, door, enginetype):
        self.window = window
        self.door = door
        self.enginetype = enginetype

    def drive(self):
        print("person drives car")


car = Car(4, 5, 'diesel')

print(dir(car))
car.drive()


class audi(Car):
    def __init__(self, window, door, enginetype, ai):
        super().__init__(window, door, enginetype)
        self.ai = ai

    def selfdrivin(self):
        print("audi supports self driving")


audiQ7 = audi(5, 4, 'petrol', True)
print(dir(audiQ7))

print(audiQ7.window)
print(audiQ7.ai)
print(audiQ7.enginetype)
print(audiQ7.selfdrivin())
'''
