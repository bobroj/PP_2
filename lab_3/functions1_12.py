def gist(ml):
    for i in range(0, len(ml), 1):
        print("*"*ml[i])

ml=[int(x) for x in (input("Введите список: ")).split()]

gist(ml)