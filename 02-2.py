a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

if (a > 0 and b < 0 and c < 0) or
   (a < 0 and b > 0 and c < 0) or
   (a < 0 and b < 0 and c > 0):
    print ("Висловлювання вірне.")
else:
    print ("Висловлювання невірне.")
