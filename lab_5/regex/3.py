import re

pattern = r'[a-z]+_[a-z]+'  

test_text = r"\nabb_ewdwd ASdasALD_ zxcXZ_zxcZ wenwekjdn_sdoifd_s_sa 0324023/'[wd_idfsd]"

x=re.findall(pattern, test_text)

print (x)