a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

if a > b:
    print(a, b)
elif b > a:
    print(b, a)
else:
    print("Ви впевнені, що ввели не однакові числа?")