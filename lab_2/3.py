# Python lists

thislist = ["apple", "banana", "cherry"]
print(thislist)

print ("-------------")

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

print ("-------------")

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

print ("-------------")

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print ("-------------")

list1 = ["abc", 34, True, 40, "male"]
print (list1)

print ("-------------")

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

print ("-------------")

tthislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(tthislist)

print ("-------------")

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

print ("-------------")

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

print ("-------------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

print ("-------------")

print(thislist[:4])

print ("-------------")

print(thislist[2:])

print ("-------------")

print(thislist[-4:-1])

print ("-------------")

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print ("-------------")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"                     #замена одного элемента листа
print(thislist)

print ("-------------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print ("-------------")

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print ("-------------")

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#добавление элемента в определенное место листа

print ("-------------")

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# добавление элемента в конец листа

print ("-------------")

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#добавление листа в лист

print ("-------------")

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#можно добавлять не только лист

print ("-------------")

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# udalenie iz lista

print ("-------------")

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#udalyaet tolko perviy banana

print ("-------------")

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#udalyaet po indeksu

print ("-------------")

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#udalit posledniy element

print ("-------------")

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#tozhe udalayet po indeksu

print ("-------------")

thislist = ["apple", "banana", "cherry"]
del thislist
#udalit ves list

print ("-------------")

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#otchistka lista

print ("-------------")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#vivod lista cherez for
   
print ("-------------")

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#vivod cherez for po indeksam
  
print ("-------------")

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#cherez while
  
print ("-------------")

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#korotkiy variant for

print ("-------------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#dobavit v noviy list tolko elementi s a

print ("-------------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#tozhe tolko koroche

print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")


