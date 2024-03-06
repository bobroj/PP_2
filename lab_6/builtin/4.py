from time import sleep
from math import sqrt

x=int(input("Введите число: "))
sec=int(input("Сколько спать? "))

sleep(sec/1000)

print(sqrt(x))