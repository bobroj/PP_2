import json

file=open("ex.json")

example=file.read()

vn=json.loads(example) #преобразование джейсона в объект питона

vn["primer"]=0
vn["proverka"]="onet"

example=json.dumps(vn, indent=4) #преобразование обратно в джсон и индент-отступы в новом файле

file=open("newfile.json", "w")

file.write(example)

print(vn)