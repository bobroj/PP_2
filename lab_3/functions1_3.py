heads=int(input("Введите количество голов:"))
legs=int(input("Введите количество лап:"))

def solve (heads, legs):
    kuri=0
    kroli=0

    kroli=(legs-2*heads)/2
    kuri=heads-kroli

    print("Курей: ", kuri, " Кроликов: ", kroli)

solve (heads, legs)    

