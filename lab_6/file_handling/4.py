import os

def count (txt_path):
    with open (txt_path, "r") as file:
        x=file.readlines()
        print(len(x))

txt_path = r"C:\PP_2\lab_6\file_handling\1.txt"

count(txt_path)
