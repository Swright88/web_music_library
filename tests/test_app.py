# ```
# # Scenario 1
# ```
# # GET /artists
# #  Expected response (200 OK):
# """
# Pixies, ABBA, Taylor Swift, Nina Simone
# """
# ```
# # Scenario 2
# ```
# # POST /artists
# #  Parameters:
# #    artist_name:   Wild nothing
# #    genre: Indie
# #  Expected response (200 OK):
# """
#         (No content)
# """
# ```
# # Scenario 3 
# ```
# GET /artists
# # Expected response (200 OK)
# Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing


def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

def test_post_artist(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    post_response = web_client.post("/artists", data= {
        'artist_name': 'Wild nothing', 
        'genre': 'Indie'
        })

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"