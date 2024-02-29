import re

pattern = "ab{2,3}"

test_string = "abbbsaasdabb"

x=re.findall(pattern, test_string)

print (x)