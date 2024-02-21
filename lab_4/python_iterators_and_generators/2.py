def even(x):
    for i in range (2, x+1, 2):
        yield i

x=int(input("Введите число: "))

for i in even(x):
    print(i)