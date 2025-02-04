# single-level inheritance

class Apple:
    manufacturer = "Apple Inc."
    contactWebsite = "www.google.com"

    def contactDetails(self):
        print("To contact us, log to ", self.contactWebsite)

class MacBook(Apple):
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print("this Macbook was made in year {} by {}".format(self.yearOfManufacture, self.manufacturer))

macbook = MacBook()
macbook.manufactureDetails()
macbook.contactDetails()



# multiple inheritance

class OperatingSystem:
    multitasking = True
    name = "MacOS"
class Brand:
    website = 'www.apple.com'
    name = "Apple"

class Ipad(Brand, OperatingSystem):
    def __init__(self):
        if self.multitasking is True:
            print("This is a multi tasking system. Visit {} for details".format(self.website))
            print("Name: ",self.name)

ipad = Ipad()



# multi-level inheritance

class MusicalInstruments:
    numberofKeys = 12

class StringIntruments(MusicalInstruments):
    typeofwood = "tonewood"

class Guitar(StringIntruments):
    def __init__(self):
        self.numberofStrings = 6
        print("This guitar consists of {} strings and made of {} and can play {} keys.".format(self.numberofStrings,self.typeofwood,self.numberofKeys))

guitar = Guitar()
