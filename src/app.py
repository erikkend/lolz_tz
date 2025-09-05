from fastapi import FastAPI
from .database import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lightweight API client")
