import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys


service_url = "https://py4e-data.dr-chuck.net/opengeo?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect("01_geodata(assignment)_db.sqlite")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Location (address TEXT, geodata TEXT)""")

# Ignore SSL Certification Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where1.data")
count = 0
not_found = 0
for line in fh:
    if count > 100:
        print("Retrieved 100 locations, restart to retrieve more.")
        break

    address = line.strip()
    print("")
    cur.execute(
        """SELECT geodata FROM Location WHERE address = ? """,
        (memoryview(address.encode()),),
    )

    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue
    except:
        pass

    params = dict()
    params["q"] = address

    url = service_url + urllib.parse.urlencode(params)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print(f"Retrieved", len(data), "character", data[:20].replace("\n", " "))
    count += 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if not js or "features" not in js:
        print("==== Download Error ====")
        print(data)
        break

    if len(js["features"]) == 0:
        print("==== Object Not Found ====")
        not_found += 1

    cur.execute(
        """INSERT INTO Location (address, geodata) VALUES ( ?, ? )""",
        (memoryview(address.encode()), memoryview(data.encode())),
    )

    conn.commit()

    # if count % 10 == 0:
    # print("Pausing for a bit....")
    # time.sleep(5)

if not_found > 0:
    print("Number of features for which locations could not be found:", not_found)
print("")
print(
    "Run geodump.py to read the data from the database so you can visualize it on a map."
)
