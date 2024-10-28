#!/usr/bin/env python3

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import json
import os

app = FastAPI()

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
