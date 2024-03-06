ex='ProVErOchNAyaStroKa'

upc=sum(1 for char in ex if char.isupper())
lwc=sum(1 for char in ex if char.islower())

print("Заглавных букв: ", upc)
print("Строчных букв: ", lwc)