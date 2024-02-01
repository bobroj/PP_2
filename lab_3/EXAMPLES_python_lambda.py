x = lambda a : a + 10
print(x(5))
#лямбда функции - анонимные функции, которые могу содержать только одно выражение

divider = "-------------"
print(divider)

x = lambda a, b : a * b
print(x(5, 6))

print(divider)

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#лямбда функция с 3 аргументами

print(divider)

def myfunc(n):
  return lambda a : a * n
#лямбда функции удобны для использования в больших функциях

print(divider)

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
#создали функцию-удвоитель 

print(divider)

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
#функция удваивает и утраивает входные данные


