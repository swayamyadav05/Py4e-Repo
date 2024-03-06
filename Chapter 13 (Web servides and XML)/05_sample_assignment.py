import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

address1 = "http://py4e-data.dr-chuck.net/comments_1968510.xml"
count = 0
sum = 0

address = input("Enter location: ")
if len(address) < 1:
    url = address1
else:
    url = address

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print("Retrieving", url)
data = urllib.request.urlopen(url, context=ctx).read()
# print(data)
print("Retrieved", len(data), "characters")
root = ET.fromstring(data)
# print(root)
# print(root.tag)
for element in root.iter("comment"):
    sum = sum + int(element.find("count").text)
    count += 1

print("Count:", count)
print("Sum:", sum)
