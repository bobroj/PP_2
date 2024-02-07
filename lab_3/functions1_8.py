def JB (my_list):
    n=len(my_list)
    
    zero1=None
    zero2=None
    seven=None

    for i in range (0, n, 1):
        if my_list[i]==0:
            if zero1==None:
                zero1=i

            elif zero2==None:
                zero2=i

        elif my_list[i]==7:
            seven=i

    if zero1!=None and zero2!=None and seven!=None and zero1<zero2<seven :

        return True
    
    return False

            

        
my_list=[int(x) for x in input("Введите список: ").split()]

if JB (my_list):
    print("True")
else:
    print ("False")
