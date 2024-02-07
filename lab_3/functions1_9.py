import math
def volume (r):
    V=4/3*math.pi*r**3

    print ("Объем сферы: ", V)

r=int(input("Введите радиус сферы: "))

volume(r)