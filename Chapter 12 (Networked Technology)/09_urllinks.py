# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certification error
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter - ")
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# # Retrieve all of the anchor tags
# tags = soup("a")
# for tag in tags:
#     print(tag.get("href", None))


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
print(tags)
for tag in tags:
    print(tag.get("href", None))

# x = "<p>Please click <a href='http://www.dr-chuck.com'>here</a></p>"
# y = re.findall(r"href='(.+)'", x)
# print(y)
