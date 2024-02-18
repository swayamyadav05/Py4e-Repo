# The Regex Version

import re

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('@([^ ]*)', line)
print(y)

y = re.findall('^From .*@([^ ]*)', line)
print(y)

y = re.findall('\S+?@\S+', line)
print(y)