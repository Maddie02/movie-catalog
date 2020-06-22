from database import DB

class Movie(object):
    def __init__(self, id, name, genre, release_year, duration, description, rating, director_name):
        self.id = id
        self.name = name
        self.genre = genre
        self.release_year = release_year
        self.duration = duration
        self.description = description
        self.rating = rating
        self.director_name = director_name


    @staticmethod
    def all():
        with DB() as db:
            movies = db.execute('SELECT * FROM movie').fetchall()
            return [Movie(*movie) for movie in movies];

    @staticmethod
    def latest():
        with DB() as db:
            movies = db.execute('''
                SELECT * FROM movie
                ORDER BY release_year DESC
            ''').fetchall()
            return [Movie(*movie) for movie in movies];

    @staticmethod
    def top10():
        with DB() as db:
            movies = db.execute('''
                SELECT * FROM movie
                ORDER BY rating DESC
            ''').fetchmany(10)
            return [Movie(*movie) for movie in movies]

    @staticmethod
    def topInGenre(genre):
        with DB() as db:
            movies = db.execute('''
                SELECT * FROM movie
                WHERE genre LIKE ?
                ORDER BY rating DESC
            ''', (genre,)).fetchall()
            return [Movie(*movie) for movie in movies]

    @staticmethod
    def create(self):
        with DB() as db:
            values = (self.name, self.genre, self.release_year, self.duration, self.description, self.rating, self.director_name)
            db.execute('''
                INSERT INTO movie (name, genre, release_year, duration, description, rating, director_name)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', values)
            return self

    @staticmethod
    def find(id):
        with DB() as db:
            movie = db.execute(
                'SELECT * FROM movie WHERE id = ?',
                (id,)
            ).fetchone()
            return Movie(*movie)