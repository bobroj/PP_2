fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#baza
  
print ("-------------")

for x in "banana":
  print(x)
#korotkiy dlya stroki
  
print ("-------------")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#ostanovka fora print do
  
print ("-------------")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#ostanovka fora print posle

print ("-------------")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#continue
  
print ("-------------")

for x in range(6):
  print(x)
#zadali range
  
print ("-------------")

for x in range(2, 6):
  print(x)
#eshe range
  
print ("-------------")

for x in range(2, 30, 3):
  print(x)
# zadali tipa increment v for korotko
  
print ("-------------")

for x in range(6):
  print(x)
else:
  print("Finally finished!")
#uslovie na konets fora
  
print ("-------------")

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#na 3 break i vse

print ("-------------")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#nested for
    
print ("-------------")

for x in [0, 1, 2]:
  pass
#pass chtob cycle ne bil pust
