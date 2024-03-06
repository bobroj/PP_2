import os

def add (txt_path):
    with open (txt_path, "a") as file:
        ls=["list", "of", "smth"]
        
        file.write("\n")

        for i in ls:
            file.write(' '+str(i))

txt_path = r"C:\PP_2\lab_6\file_handling\1.txt"

add(txt_path)