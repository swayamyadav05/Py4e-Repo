import urllib.request, urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "http://py4e-data.dr-chuck.net/comments_42.json"
address = "http://py4e-data.dr-chuck.net/comments_1968511.json"

location = input("Enter location: ")
if len(location) < 1:
    url = address
else:
    url = location

print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx).read()
data = uh.decode()
print("Retrieved", len(data), "characters")

info = json.loads(data)

# print(json.dumps(info["comments"], indent=4))

comment_count = len(info["comments"])
print("Count:", comment_count)

comment_sum = 0
for element in info["comments"]:
    comment_sum += int(element["count"])
print("Sum: ", comment_sum)
