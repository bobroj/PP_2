import re

pattern = r'[A-Z][a-z]+'

test_text = r"\nabb_ewdwd ASdasALD_ Asssa aSSaaa zxcXZ_zxcZ wenwekjdn_sdoifd_s_sa 0324023/'[wd_idfsd]"

x=re.findall(pattern, test_text)

print (x)