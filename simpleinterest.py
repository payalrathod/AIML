import datetime

principle = int(input("Enter the amount of loan: "))
years = int(input("Enter the number of years of loan: "))

enter_start_date = input('Enter the start date of loan in YYYY/MM/DD format: ')
syear, smonth, sday = map(int, enter_start_date.split('/'))
DStart = datetime.date(syear, smonth, sday)

enter_end_date = input('Enter the end date of loan in YYYY/MM/DD format: ')
syear, smonth, sday = map(int, enter_end_date.split('/'))
DEnd = datetime.date(syear, smonth, sday)

annual_rate = float(input("Enter the interest rate: "))

amount = principle * (1 + annual_rate * years)
print("Total payment amount is(Principle+Interest): ", amount)

loan_days = (DEnd - DStart).days
print("Total days of loan period= ", (DEnd - DStart).days)


# condition1_start_date = input('Enter the start date of loan in YYYY/MM/DD format: ')
# syear, smonth, sday = map(int, condition1_start_date.split('/'))
# C1Start = datetime.date(syear, smonth, sday)
# condition1_end_date = input('Enter the end date of loan in YYYY/MM/DD format: ')
# syear, smonth, sday = map(int, condition1_end_date.split('/'))
# C1End = datetime.date(syear, smonth, sday)
#
# for i in range (C1Start.day, C1End.day):
#     Condition1 = float(input("Enter Condition1 rate: "))
#     total_charge = (principle * ((C1End - C1Start).days +1) * Condition1)/days
#     print(total_charge)
#     break
#
#
# condition2_start_date = input('Enter the start date of loan in YYYY/MM/DD format: ')
# syear, smonth, sday = map(int, condition2_start_date.split('/'))
# C2Start = datetime.date(syear, smonth, sday)
# condition2_end_date = input('Enter the end date of loan in YYYY/MM/DD format: ')
# syear, smonth, sday = map(int, condition2_end_date.split('/'))
# C2End = datetime.date(syear, smonth, sday)
#
# for i in range (C2Start.day, C2End.day):
#     Condition2 = int(input("Enter Condition2 rate: "))

def __init__(self, s1, e1, C1):
    self.s1 = s1
    self.e1 = e1
    self.C1 = C1
    # s1 = input("enter condition start date yyyy/mm/dd: ")
    s2, s3, s4 = map(int, s1.split('/'))
    s5 = datetime.date(s2, s3, s4)
    # e1 = input("enter condition end date yyyy/mm/dd: ")
    e2, e3, e4 = map(int, s1.split('/'))
    e5 = datetime.date(e2, e3, e4)

    def fine(self):
        A = self.A()
        A = (principle * (e5.day - s5.day + 1) * C1) / loan_days
        return A

    if 5 > (e5.day - s5.day) > 3:
        # C1 = int(input("Enter Condition1 rate: "))
        A = (principle * (e5.day - s5.day + 1) * C1) / loan_days
        print(A)

# def get_input(A):
#     s1 = input("enter condition start date yyyy/mm/dd: ")
#     s2, s3, s4 = map(int, s1.split('/'))
#     s5 = datetime.date(s2, s3, s4)
#     e1 = input("enter condition end date yyyy/mm/dd: ")
#     e2, e3, e4 = map(int, s1.split('/'))
#     e5 = datetime.date(e2, e3, e4)
#     if 5 > (e5.day - s5.day) > 3:
#         C1 = int(input("Enter Condition1 rate: "))
#         A = (principle * (e5.day - s5.day + 1) * C1) / loan_days
#         print(A)
#
#
# get_input()
