from flask import Flask
from flask import render_template, request, redirect

from models.movie import Movie

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/movies')
def list_movies():
    return render_template('movies.html', movies=Movie.all())


@app.route('/movies/add', methods=['GET', 'POST'])
def add_movie():
    genres = ['Romance', 'Comedy', 'Action', 'Thriller', 'Drama', 'Fantasy', 'Adventure', 'Crime', 'Sci-fi', 'Historical', 'Horror', 'Mystery', 'Philosophical', 'Political', 'Animation', 'Musical'];
    if request.method == 'GET':
        return render_template('add_movie.html', genres=genres)
    elif request.method == 'POST':
        movie = Movie(None, request.form['name'],
                            request.form['genre'],
                            request.form['release_year'],
                            request.form['duration'],
                            request.form['description'],
                            request.form['rating'],
                            request.form['director_name']);

        movie.create(movie)

        return redirect('/movies')

@app.route('/movies/latest')
def latest_movies():
    return render_template('movies.html', movies=Movie.latest(), latest=1);

if __name__ == '__main__':
    app.run()

