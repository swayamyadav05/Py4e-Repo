import sqlite3
import re


class MyDB:
    def __init__(self):
        self.db_name = "emaildb_oop.sqlite"
        self.conn = ""
        self.cur = ""
        self.fh = ""

    def db_connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()

    def create_db(self):
        self.cur.execute("DROP TABLE IF EXISTS Counts")

        self.cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

    def add_db(self, a):
        self.cur.execute("INSERT INTO Counts(org, count) VALUES(?, 1)", (a,))

    def update_db(self, a):
        self.cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (a,))

    def show_db(self):
        self.sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"
        for self.row in self.cur.execute(self.sqlstr):
            print(str(self.row[0]), self.row[1])

        self.cur.close()

    def open_file(self):
        self.fname = input("Enter file name: ")
        if len(self.fname) < 1:
            self.fname = "mbox.txt"

        self.fh = open(self.fname)

        for self.line in self.fh:
            if not self.line.startswith("From: "):
                continue
            self.line = self.line.strip()
            self.temp = re.findall("@([\w.]+)", self.line)

            if len(self.temp) > 0:
                self.domain = self.temp[0]
                self.cur.execute(
                    "SELECT count FROM Counts WHERE org = ?", (self.domain,)
                )
                self.row = self.cur.fetchone()

                if self.row is None:
                    self.add_db(self.domain)
                else:
                    self.update_db(self.domain)

                self.conn.commit()


if __name__ == "__main__":
    obj = MyDB()
    obj.db_connect()
    obj.create_db()
    obj.open_file()
    obj.show_db()
