from database import DB
from models.movie import Movie


class Actor(object):
    def __init__(self, id, first_name, last_name, birth_year):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    @staticmethod
    def create(self):
        with DB() as db:
            values = (
                self.first_name, self.last_name, self.birth_year
            )
            db.execute('''
                INSERT INTO actor (first_name, last_name, birth_year)
                VALUES (?, ?, ?)
            ''', values)
            return self

    @staticmethod
    def get_actors_movies():
        with DB() as db:
            movies = db.execute('''
                SELECT movie.*
                FROM actorMovieRelation
                INNER JOIN movie ON movie.id = actorMovieRelation.movieID
                WHERE actorMovieRelation.actorID = 3
            ''').fetchall()
        return [Movie(*movie) for movie in movies]


    @staticmethod
    def getMovieActors(movie):
        with DB() as db:
            actors = db.execute('''
                SELECT actorID
                FROM actorMovieRelation
                INNER JOIN actor ON actor.id = actorMovieRelation.actorID
                WHERE actorMovieRelation.movieID = movie.id
            ''').fetchall()
        return [Actor(*actor) for actor in actors];
