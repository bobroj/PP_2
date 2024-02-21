def div(x):
    for i in range (0, x+1, 1):
        if (i%3==0 and i%4==0):
            yield i

x=int(input("Введите число: "))

for i in div(x):
    print(i)