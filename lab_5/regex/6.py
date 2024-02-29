import re

test_text = r"\nabb_ewdw.d  ., ,x , xcx. . aaasasasb djsabasdba abd asb"

x=re.sub('[ ,.]', ':', test_text) #[сет для замены]

print (x)