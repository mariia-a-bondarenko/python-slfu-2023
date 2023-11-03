a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

if (a < b and a >= c) or (a < c and a >= b):
    print(a)
elif (b < a and b >= c) or (b > a and b >= a):
    print(b)
else:
    print(c)

