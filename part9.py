def even_or_odd(num):
    if num%2 == 0:
        return "Even {}".format(num)
    else:
        return "Odd {}".format(num)
print(even_or_odd(22))

lst = [1,2,3,4,5,6,7,88,23,45]
print(list(map(even_or_odd,lst)))

def even(i):
    if i%2==0:
        return True

lst1 = [1,2,3,4,6,7,8,76,32]
print(list(filter(even,lst1)))

print(list(filter(lambda x: x%2== 0, lst1)))

print(list(map(lambda x: x%2== 0, lst1)))