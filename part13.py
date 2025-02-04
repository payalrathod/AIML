#difference between error and exception

#a=b NameError: name 'b' is not defined

try:
    #code block where exception can occur
    #a=b
    #a=1
    #b="s"
    #c=a+b
    a = int(input("enter 1st no:"))
    b = int(input("enter 2st no:"))
    c = a/b

except NameError as ex1:
    print("The user have not defined the variable")
except TypeError:
    print("Make data type similar")
except ZeroDivisionError:
    print("invalid number")
except Exception as ex:
    print("Some problem may have occurred")
    print(ex)
else:
    print(c)
finally:
    print("execution completed") # always gets printed
    #used to close database

'''
try:
    #code block where exception can occur
    #a=b
    #a=1
    #b="s"
    #c=a+b
    a = int(input("enter 1st no:"))
    b = int(input("enter 2st no:"))
    c = a/b
    d = a+b
    e = a*b

except NameError as ex1:
    print("The user have not defined the variable")
except TypeError:
    print("Make data type similar")
except ZeroDivisionError:
    print("invalid number")
except Exception as ex:
    print("Some problem may have occurred")
    print(ex)
else:
    print(c)
    print(d)
    print(e)

'''

