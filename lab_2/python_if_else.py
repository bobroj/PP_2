a = 33
b = 200
if b > a:
  print("b is greater than a")
#baza
  
print ("-------------")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#elif kak vtoroe uslovie
  
print ("-------------")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#else
  
print ("-------------")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print ("-------------")

if a > b: print("a is greater than b")
#korotkiy varik

print ("-------------")

a = 2
b = 330
print("A") if a > b else print("B")
#korotkiy else

print ("-------------")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
#srazu 3 usloviya v odnoy stroke

print ("-------------")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
#and
  
print ("-------------")

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
#or
  
print ("-------------")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
#not

print ("-------------")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
#nested if (vlozhennie)
    
print ("-------------")

a = 33
b = 200

if b > a:
  pass
#pass dlya izbeszaniya errora

