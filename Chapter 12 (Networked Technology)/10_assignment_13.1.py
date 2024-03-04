# import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certification Error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all the span tags
spans = soup("span")
# Create a empty list for storing numbers
numbers = []
# Use for loop to go through the content in spans
for span in spans:
    # Get the string i.e. number in the span and convert it into int and append it in numbers list
    numbers.append(int(span.string))
# print(numbers)
# print(len(numbers))
print(sum(numbers))
