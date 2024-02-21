import math 

def mnogo(n, a):

    s=(n*(a**2)*math.sin(math.radians(360/n)))/(8*(math.sin(math.radians(180/n))**2))  # рассчитал формулу для многоугольников,
                                                                                       # где н больше 4 через треугольники см планш
    print("площадь многоугольника:", s)

def rect (a):

    s=a**2
    print ("площадь многоугольника:" ,s)

def tre(a):

    s=0.5*(a**2)*(math.sqrt(3))/2
    print("площадь многоугольника:", s)

n=int(input ("Введите количество сторон многоугольника: " ))
a=int(input ("Введите длину одной стороны: " ))

if n>4:
    mnogo(n, a)

if n==3:
    tre(a)

if n==4:
    rect(a)

