# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1968510.xml (Sum ends with 74)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certification erreos
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address1 = "http://py4e-data.dr-chuck.net/comments_42.xml"
address2 = "http://py4e-data.dr-chuck.net/comments_1968510.xml"
count = 0
sum = 0

address = input("Enter location: ")
if len(address) < 1:
    url = address2
else:
    url = address

print("Retrieving", url)
data = urllib.request.urlopen(url, context=ctx).read()
print("Retrievied", len(data), "characters")
root = ET.fromstring(data)

for element in root.iter("comment"):
    sum = sum + (int(element.find("count").text))
    count += 1

print("Count: ", count)
print("Sum: ", sum)
