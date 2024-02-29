import re

pattern = "ab*"

test_string = "abbbsaasd"

x=re.findall(pattern, test_string)

print (x)
        

