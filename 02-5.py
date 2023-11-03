a = int(input("Введіть рік: "))

if not a % 4 and not (not a % 100 and a % 400):
    print (a, "рік високосний.")
else:
    print (a, "рік звичайний.")