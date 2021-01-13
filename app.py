from flask import Flask
from flask import render_template, request, redirect

from models.movie import Movie
from models.actor import Actor

app = Flask(__name__)

genres = ['Romance', 'Comedy', 'Action', 'Thriller', 'Drama', 'Fantasy', 'Adventure', 'Crime', 'Sci-fi', 'Historical',
          'Horror', 'Mystery', 'Philosophical', 'Political', 'Animation', 'Musical']


@app.route('/')
def main():
    return redirect('/movies')


@app.route('/movies')
def list_movies():
    return render_template('movies.html', movies=Movie.all(), genres=genres)


@app.route('/movies/add', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'GET':
        return render_template('add_movie.html', genres=genres)
    elif request.method == 'POST':
        movie = Movie(None, request.form['name'],
                      request.form['genre'],
                      request.form['release_year'],
                      request.form['duration'],
                      request.form['description'],
                      request.form['rating'],
                      request.form['director_name'])

        movie.create(movie)

        return redirect('/movies')


@app.route('/movies/actors')
def get_actor_movies():
    movies = Actor.get_actors_movies()
    for movie in movies:
        print(movie.name)
    return "Zdr"


@app.route('/movies/latest')
def latest_movies():
    return render_template('movies.html', movies=Movie.latest(), latest=1, genres=genres)


@app.route('/top10')
def top10_movies():
    return render_template('movies.html', movies=Movie.top10(), top10=1, genres=genres)


@app.route('/top/<genre>')
def top_movie_in_genre(genre):
    return render_template('movies.html', movies=Movie.top_in_genre(genre), topGenre=1, genres=genres, genre=genre)


if __name__ == '__main__':
    app.run()
