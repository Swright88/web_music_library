import os
from lib.database_connection import get_flask_database_connection
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return ", ".join(
        f"{artist}" for artist in repository.all()
    )

@app.route('/artists', methods=['POST'])
def post_artists():
    if 'artist_name' not in request.form or 'genre' not in request.form:
        return "You need to submit a title, release_year and artist-id", 400
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None, 
        request.form['artist_name'],
        request.form['genre'])
    repository.create(artist)
    return "", 200

# @app.route('/albums', methods=['Get'])
# def get_albums():
#     connection = get_flask_database_connection(app)
#     repository = AlbumRepository(connection)
#     return "\n".join(
#         f"{album}" for album in repository.all()
#     )
    


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

