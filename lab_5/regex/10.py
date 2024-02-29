import re

def Camel_To_Snake (test_text):

    x=re.sub(r"[A-Z]",lambda x: "_" + x[0].lower(), test_text)

    print (x)

test_text=r'HereIsCamelCaseGasaGio'

Camel_To_Snake(test_text)
