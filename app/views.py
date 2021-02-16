from flask import render_template
from app import app

# Views
@app.route('/movie/<movie_id>')
def index(movie_id):

    '''
    View root page function that returns the index page and its data
    '''

    return render_template('movie.html', id = movie_id)