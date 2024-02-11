# Matching and Extractiond Data

#- re.search() returns a True/False depending on whether the string atches the regular expression
#= If we actually want the matching strings to be extracted, we us re.findall()

import re

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
y = re.findall('[AEIOU]+', x)
print(y)