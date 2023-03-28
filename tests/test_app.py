""" 
When I call POST /albums with album info 
That album is now in the list in GET /albums 
"""
# Scenario 1
# POST /albums
#  Parameters:
#    title: Iowa
#    release_year: 2001
#    artist_id: 2
#  Expected response (200 OK):
"""
        (No content)
"""
# GET /albums
#  Expected response (200 OK):
"""
Album(1, Greatest Hits, 1981, 1)
Album(2, Iowa, 2001, 2)
"""
def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums", data= {
        'title': 'Iowa', 
        'release_year': '2001', 
        'artist_id': '2'
        })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Greatest Hits, 1981, 1)\n" \
        "Album(2, Iowa, 2001, 2)"


"""
When I call GET /albums
I get a lizt of all the albums
"""
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Greatest Hits, 1981, 1)"

# Scenario 2
# POST /albums
# Expected response (400 Bad request)

def test_post_albums_no_data(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/albums")
    assert post_response.status_code == 400
    assert post_response.data.decode('utf-8') == ""\
        "You need to submit a title, release_year and artist-id"

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Greatest Hits, 1981, 1)"
