#TUPLES

thistuple = ("apple", "banana", "cherry")
print(thistuple)

print ("-------------")

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print ("-------------")

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

print ("-------------")

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print ("-------------")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print ("-------------")

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

print ("-------------")

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print ("-------------")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#indeksatsiya takaya zhe kak i v listah

print ("-------------")

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

print ("-------------")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#delaem list iz tuple

print ("-------------")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#dobavili element cherez list

print ("-------------")

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#sovmeshaem tuple

print ("-------------")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#udalenie i vse cherez list

print ("-------------")

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#unpacking tuple

print ("-------------")

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# esli dobavit * to ostavsheesya prisvoetsa kak spisok

print ("-------------")

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#esli ne v kontse

print ("-------------")

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#cycles works as in lists
  
print ("-------------")

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#multiply tuples

print ("-------------")

#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found
  
