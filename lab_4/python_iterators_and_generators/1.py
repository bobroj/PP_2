def squares(x):
    for i in range (1, x+1, 1):
        yield i*i

x=int(input ("Введите число: "))

for i in squares(x):
    print(i)
