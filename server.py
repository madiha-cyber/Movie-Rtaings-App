"""Server for movie ratings app."""

from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Display homepage."""


    return render_template('homepage.html')


@app.route('/movies')
def all_movies():
    """View all movies."""
    
    movies = crud.get_movie()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """See details about movie."""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route('/users', method=['POST'])
def register_user():
    """Create a new user."""

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')

# @app.route('/')
# def log_in():

#     email = request.form.get('email')
#     password = request.form.get('password')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
