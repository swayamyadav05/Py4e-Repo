from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
names = []
links = []
count = 4
position = 3
i = 1
# print(url)
while count > 0:
    print(f"Retrieving {i}: ", url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup("a")
    # print(anchors)
    # name = anchors[position - 1].string
    # name = anchor.string
    name = anchors[position - 1].string
    url = anchors[position - 1].get("href", None)
    # links.append(url)
    # names.append(name)
    count -= 1
    i += 1
# print(links)
# print(names)
print(name)
# print(url)
