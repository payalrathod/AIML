# custom exception

class Error(Exception):
    pass

class DOBxception(Error):
    pass

year = int(input("Enter DOB: "))
age = 2021 - year
try:
    if age <= 30 & age > 20:
        print("Valid age")
    else:
        raise DOBxception
except DOBxception:
    print("year is invalid")
