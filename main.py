from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from .db.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield create_db_and_tables()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
