# Single Table Design Recipe Template
# Music_web_app - Artist

## 1. Extract nouns from the user stories or specification

```
# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone

# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
```
```
As a music lover,
So I can organise my favourite artists,
I want to keep a list of artists

As a music lover,
So I can organise my favourite artists,
I want to be able to add a new artist and genre to the list
```
Test should assert that the new album is present in the list by calling `GET /artists`
```
Nouns:

artist, genre
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                |
| --------------------- | ------------------------  |
| artist                | id, artists_name, genre   |

Name of the table (always plural): `artists` 

Column names: `artist`, `genre`, `id`

## 3. Decide the column types.

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
artist_name: text
genre: text
```

## 4. Write the SQL.

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.


CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    artist_name text,
    genre text
)
```

## 5. Create the table.

```bash
psql -h 127.0.0.1 music_web_app < artists_table.sql
```

# {{ Music_web_app }} Route Design Recipe

## . Design the Route Signature
_Include the HTTP method, the path, and any query or body parameters._

```
POST /artists
artist_name: text
genre: text
```
```
GET /albums

## . Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
"""
```
# Scenario 1
```
# GET /albums
#  Expected response (200 OK):
"""
Album(1, Greatest Hits, 1981, 1)
Album(2, Iowa, 2001, 2)
"""
```
# Scenario 2
```
# POST /artists
#  Parameters:
#    artist_name:   Wild nothing
#    genre: Indie
#  Expected response (200 OK):
"""
        (No content)
"""
```
# Scenario 3 
```
# POST /albums
# Expected response (400 Bad request)
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


