from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src import crud, schemas
from src.database import get_db

router = APIRouter(prefix="/api_keys", tags=["api_keys"])


@router.post("/create", response_model=schemas.ApiKeyOut)
def create_apikey(data: schemas.ApiKeyCreate, db: Session = Depends(get_db)):
    api_key = crud.create_api_key(db, data.source_name)
    return {"api_key": api_key.key, "source_name": api_key.source_name}
