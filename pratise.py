def summ(n1, n2):
    n1 = int(input())
    n2 = int(input())
    product = n1 * n2
    if product >= 1000:
        return product
    else:
        return n1 + n2


a = summ(30, 20)
print(a)
