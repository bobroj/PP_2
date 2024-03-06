import os

path=input("Input the path: ")

if not os.path.exists(path):
    print("NEALLO!")

else:
    os.remove(path)
    print("File deleted")