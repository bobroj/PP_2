import re

def SnakeToCamel (test_text):
    x=re.split('_', test_text)
    
    y=[i.capitalize() for i in x] # capitalize первую букву преобразует в заглавную, а все последующие в маленькие
    
    z=''.join(y) #объединяю все элементы у без разделения

    print (z)

test_text = r"\nabb_ew vsem_privet_snake_case_CAmel woi_ds dsSDAd"

SnakeToCamel (test_text)

 