import re

pattern = r'a.*b$'

test_text = r"\nabb_ewdwd aaasasasb djsabasdba abd asb"

x=re.findall(pattern, test_text)

print (x)