import sqlite3
import csv
import os
from fastapi import FastAPI

app = FastAPI()
DB_FILE = "movies.db"


def load_data(cursor, filename, table, columns):
    if not os.path.exists(filename):
        return

    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        placeholders = ','.join(['?'] * len(columns))
        col_names = ','.join(columns)
        sql = f"INSERT INTO {table} ({col_names}) VALUES ({placeholders})"
        batch = []
        for row in reader:
            batch.append(tuple(row[col] for col in columns))
            if len(batch) >= 5000:
                cursor.executemany(sql, batch)
                batch = []
        if batch:
            cursor.executemany(sql, batch)


def initialize_database():
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()

        tables = {
            "movies": "movieId INTEGER PRIMARY KEY, title TEXT, genres TEXT",
            "links": (
                "movieId INTEGER PRIMARY KEY, imdbId TEXT, tmdbId TEXT, "
                "FOREIGN KEY(movieId) REFERENCES movies(movieId)"
            ),
            "ratings": (
                "id INTEGER PRIMARY KEY AUTOINCREMENT, userId INTEGER, "
                "movieId INTEGER, rating REAL, timestamp INTEGER, "
                "FOREIGN KEY(movieId) REFERENCES movies(movieId)"
            ),
            "tags": (
                "id INTEGER PRIMARY KEY AUTOINCREMENT, userId INTEGER, "
                "movieId INTEGER, tag TEXT, timestamp INTEGER, "
                "FOREIGN KEY(movieId) REFERENCES movies(movieId)"
            )
        }

        for name, schema in tables.items():
            cur.execute(f"CREATE TABLE IF NOT EXISTS {name} ({schema})")

        if not cur.execute("SELECT 1 FROM movies LIMIT 1").fetchone():
            load_data(
                cur, 'movies.csv', 'movies',
                ['movieId', 'title', 'genres']
            )
            load_data(
                cur, 'links.csv', 'links',
                ['movieId', 'imdbId', 'tmdbId']
            )
            load_data(
                cur, 'tags.csv', 'tags',
                ['userId', 'movieId', 'tag', 'timestamp']
            )
            load_data(
                cur, 'ratings.csv', 'ratings',
                ['userId', 'movieId', 'rating', 'timestamp']
            )

        conn.commit()


initialize_database()


def execute_query(query, args=()):
    with sqlite3.connect(DB_FILE) as conn:
        conn.row_factory = sqlite3.Row
        return conn.execute(query, args).fetchall()


@app.get("/movies")
def list_movies():
    return execute_query("SELECT * FROM movies")


@app.get("/links")
def list_links():
    return execute_query("SELECT * FROM links")


@app.get("/tags")
def list_tags():
    return execute_query("SELECT * FROM tags")


@app.get("/ratings")
def list_ratings():
    return execute_query("SELECT * FROM ratings LIMIT 100")
