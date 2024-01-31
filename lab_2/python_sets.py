thisset = {"apple", "banana", "cherry"}
print(thisset)

print ("-------------")

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#dubli ne hranit

print ("-------------")

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
# 1 i true odno i ti zhe i false s 0

print ("-------------")

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

myset = {"apple", "banana", "cherry"}
print(type(myset))

print ("-------------")

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

print ("-------------")

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#vivod cherez cycle
  
print ("-------------")

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#adding elements

print ("-------------")

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#also adding

print ("-------------")

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#update rabotaet s raznimi dannimi

print ("-------------")

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#udalenie

print ("-------------")

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#udalenie concretnogo elementa

print ("-------------")

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

print ("-------------")

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#otchistka

print ("-------------")

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#vivof for
  
print ("-------------")

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#obyedinenie

print ("-------------")

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#tozhe
