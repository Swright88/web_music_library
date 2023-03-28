from lib.album import Album

"""
Constructs with an id, title, release year and artist id
"""
def test_contructs():
    album = Album(1, "Test Title", 1000, 2)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 1000
    assert album.artist_id == 2


"""
Albums with equal contents are equal
"""
def test_compares():
    album1 = Album(1, "Test Title", 1000, 2)
    album2 = Album(1, "Test Title", 1000, 2)


def test_make_string():
    album = Album(1, "Test Title", 1000, 2)
    assert str(album) == "Album(1, Test Title, 1000, 2)"