import re

def insspaces (test_text):

    x=re.findall('[A-Z][a-z]*', test_text)
    
    y=" ".join(x)

    print (y)


test_text=r'asdijSAOIDJ zxiocjXZC Ijz JcxIksd ItsAgainTest'

insspaces (test_text)