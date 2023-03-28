from lib.album_repository import AlbumRepository
from lib.album import Album
""""
When I call #all
I get the albums in the albums table 
"""
def test_all(db_connection):
    repository = AlbumRepository(db_connection)
    assert repository.all() == [Album(1, "Greatest Hits", 1981, 1),
    Album(2, "Test Title", 1000, 3)]

"""
When I call create
I add an album to the database and return it when calling all
"""
def test_create(db_connection):
    db_connection.seed("seeds/record_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, "Test Title", 1000, 3)
    repository.create(album)
    assert repository.all() == [
        Album(1, "Greatest Hits", 1981, 1),
        Album(2, "Test Title", 1000, 3)
    ]