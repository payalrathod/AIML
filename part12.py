class Car:
    def __init__(self, window, door, enginetype):
        self.window = window
        self.door = door
        self.enginetype = enginetype

    def driving(self):
        return "this is a {} car".format(self.enginetype)


car1 = Car(4, 5, 'petrol')
car2 = Car(3, 4, 'diesel')

print(car1.window)
print(car2.door)
print(car2.enginetype)

print(car1.driving)
print(car1.driving())



'''
class Car:
    pass # no properties in class

car1 = Car()
print(dir(car1))
print(car1)

car1.windows = 5
car1.doors = 4
print(car1.windows)

car2 = Car()
car2.windows = 3
car2.doors = 2
print(car2.windows)

car2.enginetype = 'petrol'
print(car2.enginetype)
'''
