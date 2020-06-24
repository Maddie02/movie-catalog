import sqlite3

DB_NAME = 'movies.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('''
    CREATE TABLE IF NOT EXISTS movie
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255) NOT NULL,
            genre VARCHAR(20) NOT NULL,
            release_year INTEGER NOT NULL,
            duration INTEGER NOT NULL,
            description TEXT NOT NULL,
            rating REAL NOT NULL,
            director_name VARCHAR(20) NOT NULL
        )
''')

conn.cursor().execute('''
    CREATE TABLE IF NOT EXISTS actor 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            birth_year INTEGER NOT NULL
        )
''')

conn.cursor().execute('''
    CREATE TABLE IF NOT EXISTS actorMovieRelation (
        actorID INTEGER,
        movieID INTEGER,
        FOREIGN KEY (actorID) REFERENCES actor(id),
        FOREIGN KEY (movieID) REFERENCES movie(id)
    )
''')

conn.commit()

class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn.cursor()
    

    def __exit__(self, type, value, traceback):
        self.conn.commit()

