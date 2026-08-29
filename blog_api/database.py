from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

import os
from dotenv import load_dotenv


# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()


# -----------------------------------
# Database URL
# -----------------------------------

DATABASE_URL = os.getenv("DATABASE_URL")


# -----------------------------------
# Create Database Engine
# -----------------------------------

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


# -----------------------------------
# Create Session
# -----------------------------------

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# -----------------------------------
# Base Class
# -----------------------------------

Base = declarative_base()


# -----------------------------------
# Database Dependency
# -----------------------------------

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()