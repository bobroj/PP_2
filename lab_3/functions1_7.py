def proverka (my_list):

    n=len(my_list)

    if all(x == 3 for x in my_list): # all возвращает тру или фолс
        return True

    for i in range (0, n-1, 1):
        if my_list[i]==3 and my_list[i-1]==3 and my_list[i-1]!=my_list[n-1] or my_list[i+1]==3 and my_list[i+1]!=my_list[0] :
            return True
    return False
        
my_list=[int (x) for x in input("Введите список: ").split()]

if proverka(my_list):
    print("True")

else:
    print("False")

