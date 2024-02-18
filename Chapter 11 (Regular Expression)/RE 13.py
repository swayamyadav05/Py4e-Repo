# Escape Character

# If you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'

import re
x = "We just received $10.00 for cookies."
y = re.findall(r'\$[0-9.]+', x)
print(y)


# '\$[0-9.]+'

# '$' A real dollar sign
# '0-9.' A digit or period
# '+' At least one or more

