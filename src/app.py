from fastapi import FastAPI
from src.database import Base, engine
from src.routers import users, apikeys

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Test API")

app.include_router(users.router)
app.include_router(apikeys.router)
