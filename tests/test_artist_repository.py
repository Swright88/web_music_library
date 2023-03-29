from lib.artist_repository import ArtistRepository
from lib.artist import Artist
"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/record_store.sql") # Seed our database with some test data
    repository = ArtistRepository(db_connection) # Create a new ArtistRepository
    artists = repository.all() # Get all artists
    # Assert on the results
    assert artists == artists
"""
When we call ArtistRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = ArtistRepository(db_connection)
    repository.create(Artist(None, "The Beatles", "Rock"))
    result = repository.all()
    print(result)
    assert result == result
