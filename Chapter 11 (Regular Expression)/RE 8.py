# Fine-Tuning string extraction

#- You can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
