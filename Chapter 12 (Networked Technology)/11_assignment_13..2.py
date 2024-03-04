# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Flyn.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certification Error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))
i = 1

while count > 0:
    print(f"Retrieving {i}: ", url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    anchors = soup("a")
    name = anchors[position - 1].string
    url = anchors[position - 1].get("href", None)
    count -= 1
    i += 1
print(name)
