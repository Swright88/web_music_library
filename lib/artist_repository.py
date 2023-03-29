from lib.artist import Artist
class ArtistRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["artist_name"], row["genre"])
            artists.append(item)
        return artists

    # Create a new artist
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, artist):
        self._connection.execute('INSERT INTO artists (artist_name, genre) VALUES (%s, %s)', [
                                artist.artist_name, artist.genre])
        return None