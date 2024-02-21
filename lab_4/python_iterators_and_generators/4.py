def squares(a, b):
    for i in range (a, b+1, 1):
        yield i*i

a=int(input("Введите нижнюю границу: "))
b=int(input("Введите вернюю границу: "))

for i in squares(a, b):
    print (i)