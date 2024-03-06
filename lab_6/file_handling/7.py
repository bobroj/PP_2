def copy (orig):
    with open(orig, "r") as file:
        x=file.read()

    with open("copy.txt", "a") as file:
        file.write(x)

orig="1.py"
copy(orig)