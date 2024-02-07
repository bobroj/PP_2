def uniq(my_list):
    uniq_list=[]

    for i in range (0, len(my_list), 1):
        if my_list[i] not in uniq_list :
            uniq_list.append(my_list[i])

    print ("Уникальные элементы из вашего списка: ", uniq_list)

my_list=[int(x) for x in input("Введите список: ").split()]

uniq(my_list)