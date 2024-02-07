def is_palimdrome(sen):
    for i in range (0, len(sen)//2, 1):
        if sen[i]!=sen[len(sen)-i-1] :
            return False
        
    return True


sen=input("Введите слово/предложение: " )

if is_palimdrome(sen) is True :
    print ("Palindrome")
else :
    print ("Not palindrome")
