# import datetime
#
# principle = int(input("Enter the amount of loan: "))
# years = int(input("Enter the number of years of loan: "))
#
# enter_start_date = input('Enter the start date of loan in YYYY/MM/DD format: ')
# syear, smonth, sday = map(int, enter_start_date.split('/'))
# DStart = datetime.date(syear, smonth, sday)
#
# capital_charge = float(input("Enter the interest rate: "))
#
# rn = []  # rate of interest array
# sn = []
# en = []
#
# ncondition = int(input("Enter the number of conditions: "))
#
# def get_input():
#     rate = float(input("Enter rate for condition: "))
#     start_date = input('Enter the start date of loan in YYYY/MM/DD format: ')
#     syear, smonth, sday = map(int, start_date.split('/'))
#     start = datetime.date(syear, smonth, sday)
#     end_date = input('Enter the end date of loan in YYYY/MM/DD format: ')
#     syear, smonth, sday = map(int, end_date.split('/'))
#     end = datetime.date(syear, smonth, sday)
#     return rate, start, end
#
#
# for i in range (1,ncondition+1):
#     if i == 1:
#         rate, start, end = get_input()
#         total_charge = (principle * ((end - start).days + 1) * rate) / (years * 365)
#         print(total_charge)
#         rn.append(rate)
#         print("RN: ",rn)
#     if i >= 2:
#         rate, start, end = get_input()
#         CP1 = (principle * ((end - start).days +1) * rate) / (years * 365)
#         print(CP1)
#         rn.append(rate)
#         print("RN: ",rn)
#
#

# import sys
# print('py {}'.format(sys.version))
# # import scipy
# # print('scipy {}'.format(scipy.version))
# import numpy
# print('nump {}'.format(numpy._version))
# import matplotlib
# print('matplot {}'.format(matplotlib._version))
# import pandas
# print('pandas {}'.format(pandas._version))
# # import sklearn
# # print('skle {}'.format(sklearn.__version__))



