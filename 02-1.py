a = int(input("Введіть число: "))

print("Варіант 1:")
if a % 2 > 0:
    print ("True")
else:
    print ("False")

print("Варіант 2:")
print(bool(a % 2))
