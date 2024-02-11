# Non-Greedy Matching 

#- Not all regular expression repeat codes are greedy!
#- If you add a '?' character, the + and * chill out a bit...

import re
x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)

