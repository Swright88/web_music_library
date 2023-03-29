from lib.artist import Artist

"""
Constructs with an id, artist_name and genre
"""
def test_contructs():
    artist = Artist(1, "Test name", "Test Genre")
    assert artist.id == 1
    assert artist.artist_name == "Test name"
    assert artist.genre == "Test Genre"


"""
Artists with equal contents are equal
"""
def test_compares():
    artist1 = Artist(1, "Test name", "Test Genre")
    artist2 = Artist(1, "Test name", "Test Genre")


def test_make_string():
    artist1 = Artist(1, "Test name", "Test Genre")
    assert str(artist1) == "Test name"