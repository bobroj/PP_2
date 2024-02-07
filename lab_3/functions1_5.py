from itertools import permutations

def print_permutations(string):
    # генерируем строки
    permuted_strings = permutations(string)

    # выводим каждую перестановку
    for perstring in permuted_strings:
        print(''.join(perstring)) #джоин объединяет символы в строку без пробелов, тк изначачально она представлена в виде кортежа

vvod_string = input("Введите строку: ")

print_permutations(vvod_string)
