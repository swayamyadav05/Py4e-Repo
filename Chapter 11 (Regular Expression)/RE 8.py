# Fine-Tuning string extraction

#- You can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses

# Parentheses are not part of the match -but they tell where to start and stop what string to extract

import re
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall(r'\S+@\S+', x)
print(y)
y = re.findall(r'^From (\S+@\S+)', x)
print(y)
y = re.findall(r'^From .*@(\S+)', x)
print(y)
