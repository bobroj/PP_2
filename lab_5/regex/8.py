import re

pattern = r'[A-Z][^A-Z ]*' #все кроме еще заглавных или пробела

test_text = r"\na EtoItsJust s a TestPrit"

x=re.findall(pattern, test_text)

y=' '.join(x)

print (y)