import sqlite3

conn = sqlite3.connect("db_assignment_15.sqlite")
cur = conn.cursor()

cur.executescript(
    """
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id   INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE,
    album_id    INTEGER,
    genre_id    INTEGER,
    len INTEGER, count  INTEGER, rating INTEGER
);
"""
)

handle = open("tracks.csv")


for line in handle:
    line = line.strip()
    pieces = line.split(",")
    if len(pieces) < 7:
        continue
    # Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Rock
    #              0               1          2       3  4    5     6

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    # print(name, artist, album, count, rating, length, genre)

    cur.execute(
        """
            INSERT OR IGNORE INTO Artist ( name ) VALUES ( ? )""",
        (artist,),
    )
    cur.execute(
        """
                SELECT id FROM Artist WHERE name = ? """,
        (artist,),
    )
    artist_id = cur.fetchone()[0]

    cur.execute(
        """
                INSERT OR IGNORE INTO Genre ( name ) VALUES ( ? )""",
        (genre,),
    )
    cur.execute(
        """
                SELECT id FROM Genre WHERE name = ? """,
        (genre,),
    )
    genre_id = cur.fetchone()[0]

    cur.execute(
        """
                INSERT OR IGNORE INTO Album ( title, artist_id ) VALUES ( ?, ? )""",
        (album, artist_id),
    )
    cur.execute(
        """
                SELECT id FROM Album WHERE title = ? """,
        (album,),
    )
    album_id = cur.fetchone()[0]

    cur.execute(
        """
                INSERT OR REPLACE INTO Track ( title, genre_id, album_id, len, rating, count )VALUES ( ?, ?, ?, ?, ?, ? )""",
        (name, genre_id, album_id, length, rating, count),
    )

    conn.commit()

sqlstr = """
SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id AND Album.artist_id = Artist.id ORDER BY Artist.name LIMIT 3
"""
# """SELECT Track.title, Artist.name, Album.title, Genre.name FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.id AND Track.album_id = Album.id AND Album.artist_id = Artist.id ORDER BY Artist.name LIMIT 3"""

for row in cur.execute(sqlstr):
    print(f"{str(row[0])} | {str(row[1])} | {str(row[2])} | {str(row[3])}")

cur.close()
