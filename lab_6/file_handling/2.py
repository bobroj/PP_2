import os

def check(path):

    if not os.path.exists(path):
        print("Path doesnt exist")
        return
    
    print("Path exists")
    
    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not readable")
    
    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not writable")
    
    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not executable")

path= input("Введите путь к файлу: ")

check(path)
