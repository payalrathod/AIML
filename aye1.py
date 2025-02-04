sq = [1,4,9,16,25]
# print(sq)
# print(sq[-1])
# print(sq[-3:0])
# print(sq + [2,3,6,8])
sq1 = sq + [12,34,56,78]
# print(sq1)
sq[3] = 100
# print(sq)
sq1.append(123)
# print(sq1)
# print(len(sq1))
x = [sq,sq1]
# print(x)
# print(x[1][3])
y = [x**2 for x in range(10)]
# print(y)

# tuples
t = 2, 45, 'hello'
print(t)
u = t, (1,2,3,4,5)
print(u)
i = ()
print(len(i))
print(len(t))
v = tuple([12,2,34,5,67,8])
print(v)
print(tuple([x**2 for x in range(10)]))

# sets
# s =