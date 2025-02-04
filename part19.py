import datetime
now = datetime.datetime.now()
print(now.year)
class Car:
    base1 = 100000

    def __init__(self, window, door, power):
        self.window = window
        self.door = door
        self.power = power

    def what_base_price(self):
        print("base price: {}".format(self.base1))

    @classmethod
    def revise_base_price(cls, inflation):
        cls.base1 = cls.base1 + (cls.base1 * inflation)
        print(cls.base1)
    @staticmethod
    def check_year():
        if now.year == 2021:
            return True
        else:
            return False
print(Car.check_year())
car1 = Car(4,5,2000)
if car1.check_year():
    pass
else:
    print(Car.revise_base_price())

#class methods
'''
class Car:
    base1 = 100000

    def __init__(self, window, door, power):
        self.window = window
        self.door = door
        self.power = power

    def what_base_price(self):
        print("base price: {}".format(self.base1))

    @classmethod
    def revise_base_price(cls, inflation):
        cls.base1 = cls.base1 + (cls.base1 * inflation)
        print(cls.base1)


# car1 = Car(4, 5, 2000)
# print(car1.base)
Car.revise_base_price(0.10)   # for good practise
car1 = Car(4,5,2000)
print(car1.base1)

car1.revise_base_price(0.10)
print(car1.base1)

'''