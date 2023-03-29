# Single Table Design Recipe Template
# Music_web_app

## 1. Extract nouns from the user stories or specification

```
# Request
Post /albums

# With body parameters:
title=Voyage
release_yeat=2022
artist_id=2

# Expected response (200 OK)
(No content)
```
```
As a music lover,
So I can organise my records,
I want to keep a list of albums' titles.

As a music lover,
So I can organise my records,
I want to keep a list of albums' release year.
```
Test should assert that the new album is present in the list by calling `GET /albums`
```
Nouns:

album, title, release year, artist id
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                         |
| --------------------- | ---------------------------------  |
| album                 | id, title, release year, artist id |

Name of the table (always plural): `albums` 

Column names: `title`, `release_year`, `artist_id`, `id`

## 3. Decide the column types.

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int
```

## 4. Write the SQL.

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);
```

## 5. Create the table.

```bash
psql -h 127.0.0.1 music_web_app < albums_table.sql
```

# {{ Music_web_app }} Route Design Recipe

## . Design the Route Signature
_Include the HTTP method, the path, and any query or body parameters._

```
POST /albums
title: string
release_year: number (str)
artist_id: number (str)
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
# POST /albums
#  Parameters:
#    title: Iowa
#    release_year: 2001
#    artist_id: 2
#  Expected response (200 OK):
"""
        (No content)
"""
```
# Scenario 2
```
# GET /albums
#  Expected response (200 OK):
"""
Album(1, Greatest Hits, 1981, 1)
Album(2, Iowa, 2001, 2)
"""
```
# Scenario 3 
```
# POST /albums
# Expected response (400 Bad request)
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


