import mysql.connector
from mysql.connector import Error

#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os
from fastapi.middleware.cors import CORSMiddleware

DBHOST = "ds2022.cqee4iwdcaph.us-east-1.rds.amazonaws.com"
DBUSER = "ds2022"
DBPASS = os.getenv('DBPASS')
DB = "yxb8mh"

try:
    db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, 
database=DB)
    cur = db.cursor()
    print("Database connection successful!")
except Error as e:
    print(f"Error connecting to the database: {e}")


app = FastAPI()

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI with MySQL and CORS!"}


@app.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API!!!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@app.get("/square/{a}")
def square(a: int):
    return {"result": a * a}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Carrie Feng",
        "email": "yxb8mh@virginia.edu"
    }

@app.get("/genres")
def get_genres():
    query = "SELECT * FROM genres ORDER BY genreid;"
    try:    
        cur.execute(query)
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = [dict(zip(headers, result)) for result in results]
        return json_data
    except Error as e:
        return {"Error": f"MySQL Error: {e}"}

@app.get("/songs")
def get_songs():
    query = """
    SELECT 
        songs.title, 
        songs.album, 
        songs.artist, 
        songs.year, 
        songs.file, 
        songs.image, 
        genres.genre 
    FROM songs 
    JOIN genres 
    ON songs.genre = genres.genreid
    ORDER BY songs.id;
    """
    try:
        cur.execute(query)
        headers = [x[0] for x in cur.description]
        results = cur.fetchall()
        json_data = [dict(zip(headers, result)) for result in results]
        return json_data
    except Error as e:
        return {"Error": f"MySQL Error: {e}"}
