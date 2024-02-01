thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#sozdali i viveli dictionary

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#dostaem nuzhnoe znachenie po kluchu

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#delaem 2 znacheniya vivedet tolko poslednee

print ("-------------")

print(len(thisdict))

print ("-------------")

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
#podderzhivaet raznie type 

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
#dictionary type

print ("-------------")

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#sposob s ()

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print (x)

#vizov po kluchu

print ("-------------")
print (x)

x = thisdict.get("model")
#viziv znacheniy

print ("-------------")

x = thisdict.keys()
print (x)
#viziv klucha

print ("-------------")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
#mozhno menyat dannie

print ("-------------")

x = thisdict.values()
print (x)
#poluchit' values

print ("-------------")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#menyaem znacheniya

print ("-------------")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
#dobavlyaem i menyaem tsvet

print ("-------------")

x = thisdict.items()
print (x)
#poluchenie i kluchey i znacheniy

print ("-------------")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

print ("-------------")

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

print (thisdict)
#menyaem odno znachenie

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
#cherez update

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#dobavili znacheniya

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
#tozhe cherez update

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#udalenie s pop

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#udalenie s popitem

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#s del
   
print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#s clear

print ("-------------")

for x in thisdict:
  print(x)
#vivod cherez cycle
  
print ("-------------")

for x in thisdict:
  print(thisdict[x])
#drugoy var
  
print ("-------------")

for x in thisdict.values():
  print(x)
#values
  
print ("-------------")

for x in thisdict.keys():
  print(x)
#keys cherez cycle

print ("-------------")

for x, y in thisdict.items():
  print(x, y)
#i to t drugoe cherez loop

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#copy dict

print ("-------------")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#drugoy sposob

print ("-------------")

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print (myfamily)
#nested dictionaries (vlozhennie dict)

print ("-------------")

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print (myfamily)
#tree dict

print ("-------------")

print(myfamily["child2"]["name"])

print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")

print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")
print ("-------------")