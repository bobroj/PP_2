def back (x):
    for i in range (x, -1, -1):
        yield i

x=int(input("Введите номер: "))

for i in back(x):
    print(i, end=", ")