from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from contextlib import asynccontextmanager

import certifi

from .env import MONGO_DB_USERNAME, MONGO_DB_PASSWORD

@asynccontextmanager
async def lifespan(app: FastAPI):
    await startup_db_client(app)
    yield
    await shutdown_db_client(app)

async def startup_db_client(app: FastAPI) -> MongoClient:
    try:
        app.client = MongoClient(f'mongodb+srv://{MONGO_DB_USERNAME}:{MONGO_DB_PASSWORD}@cluster0.iut8m.mongodb.net/', tlsCAFile=certifi.where())
        app.db = app.client.get_database("fetch")
        print("Connected to fetch database.")
    except Exception as exception:
        print("Cannot connect to fetch database.")

async def shutdown_db_client(app: FastAPI) -> None:
    app.client.close()
    print('Database disonnected.')
