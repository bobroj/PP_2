import os

path_to_folder= r"C:/Program Files/AMD/AMD Privacy View"

list=os.listdir(path_to_folder)
papki=[]
files=[]

print("Все, что есть: ", list) #вернет список и файлов и папок

for x in list:
    if os.path.isfile(x):
        files.append(x)

    else:
        papki.append(x)

print("Только файлы: ", files)
print("Только папки: ", papki)

