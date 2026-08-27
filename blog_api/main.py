from fastapi import FastAPI

from database import Base, engine
from routers.auth import router as auth_router
from routers.posts import router as posts_router

import models


# -----------------------------------
# Create Database Tables
# -----------------------------------

Base.metadata.create_all(bind=engine)


# -----------------------------------
# FastAPI Application
# -----------------------------------

app = FastAPI(
    title="Blog API"
)


# -----------------------------------
# Include Routers
# -----------------------------------

app.include_router(auth_router)
app.include_router(posts_router)