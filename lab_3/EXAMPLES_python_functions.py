def my_function():
  print("Hello from a function")

my_function()
#bazoviy primer function

print ("-------------")

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
#v skobkah peredavaemie dannie

print ("-------------")

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
#mozhet prinimat' neskol'ko argumentov
divider = "-------------"
print(divider)

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#если неизвестно число передаваемых аргументов, можно использовать * (кортеж)
print(divider)

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#обращаемся по ключу

print(divider)

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
#если передаются значения ключ-значение в неизвестном количестве, то можно использовать **

print(divider)

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#при создании defolt parametr () функция использует значение, прописанное в ней

print(divider)

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
# peredavat mozhno raznie tipi dannih

print(divider)

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
# return возвращает результат работы функции

print(divider)

def myfunction():
  pass
#pass dlya zapolneniya pustot

print(divider)

def my_function(x, /):
  print(x)

my_function(3)
#будет принимать только позиционные аргументы, не принимает ключевые из-за /

print(divider)

def my_function(x):
  print(x)

my_function(3)
#передаем ключевое значение 

print(divider)

def my_function(*, x):
  print(x)

my_function(x = 3)
#принимает только ключевые аргументы из-за *

print(divider)

def my_function(x):
  print(x)

my_function(3)
#без * принимает только позиционные аргументы

print(divider)

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

#можно миксовать / и * все, что написано до / передается как positional only, все что до * передается только как key-word only








