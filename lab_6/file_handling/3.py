import os

def test_path(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return
    
    print("Path exists")
    
    filename = os.path.basename(path) # извлечение файла по этому пути
    directory = os.path.dirname(path) # фрагмент пути к папке
    
    print("Filename:", filename)
    print("Directory:", directory)

path = input("Enter the path: ")
test_path(path)
