import sqlite3
import re

conn = sqlite3.connect("emaildb1.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute(
    """
            CREATE TABLE Counts (org TEXT, count INTEGER)"""
)

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox.txt"
fh = open(fname)
for line in fh:
    line = line.rstrip()
    orgs = re.findall(r"^From .*@(\S+)", line)
    for org in orgs:

        cur.execute("SELECT count FROM Counts WHERE org = ? ", (org,))
        row = cur.fetchone()
        if row is None:
            cur.execute(
                """
                        INSERT INTO Counts (org, count) VALUES (?, 1)""",
                (org,),
            )
        else:
            cur.execute(
                """
                        UPDATE Counts SET count = count + 1 WHERE org = ? """,
                (org,),
            )
    conn.commit()

# https://www.sqlite.org/lang_select.html

sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
