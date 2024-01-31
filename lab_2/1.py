#Boolean

print (10>9)
print (10==9)
print (10<9)

a=200
b=23

if b>a:
    print ("b is greater than a")

else:
    print ("b is smaller than a")


print(bool("Hello"))
print(bool(15))

po=""
print(bool(po))

print("-------------")


class myclass():
    def __len__(self):
        return 0
    
myobj=myclass()
print (bool(myobj))

print ("-------------")

def myfunct() :
    return True

print (myfunct())

print ("-------------")

def param () :
    return True

if param :
    print ("YES")

else :
    print ("NO")

print ("-------------")

x=200

print (isinstance (x, int))

print ("-------------")

