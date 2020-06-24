from database import DB

class Actor(object):
    def __init__(self, id, first_name, last_name, birth_year):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    @staticmethod
    def getActorMovies(actor):
        with DB() as db:
            movies = db.execute('''
                SELECT movieID
                FROM actorMovieRelation
                INNER JOIN movie ON movie.id = actorMovieRelation.movieID
                WHERE actorMovieRelation.actorID = actor.id
            ''').fetchall()
        return [Movie(*movie) for movie in movies];

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
