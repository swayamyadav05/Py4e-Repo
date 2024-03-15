import sqlite3
import json
import codecs

conn = sqlite3.connect("01_geodata(assignment)_db.sqlite")
cur = conn.cursor()

cur.execute("SELECT * FROM Location")
fhand = codecs.open("01_where.js", "w", "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur:
    data = str(row[1].decode())
    try:
        js = json.loads(str(data))
    except:
        continue

    if len(js["features"]) == 0:
        continue

    try:
        lat = js["features"][0]["geometry"]["coordinates"][1]
        lon = js["features"][0]["geometry"]["coordinates"][0]
        where = js["features"][0]["properties"]["display_name"]
        where = where.replace("'", "")
    except:
        print("Unexpected Format")
        print(js)

    try:
        print(where, lat, lon)

        count += 1
        if count > 1:
            fhand.write(",\n")
        output = "[" + str(lat) + ", " + str(lon) + ", '" + where + "']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to 01_where.js")
print("Open where.html to view the data in a browser.")
