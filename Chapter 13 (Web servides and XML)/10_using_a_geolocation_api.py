import urllib.request, urllib.parse
import json, ssl

serviceurl = "http://py4e-data.dr-chuck.net/opengeo?"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    address = address.strip()
    parms = dict()
    parms["q"] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    print("Retrieved", len(data), "characters")

    json_data = json.loads(data)
    # print(json.dumps(json_data["features"][0]["properties"]["plus_code"], indent=4))

    plus_code = json_data["features"][0]["properties"]["plus_code"]
    print("Plus code", plus_code)
