from fastapi import FastAPI

from app.routers import breeds

app = FastAPI()

app.include_router(breeds.router)
