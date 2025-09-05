from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from src import schemas, crud
from src.database import get_db
from src.dependencies import get_api_key
from src.models import ApiKey


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/create", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db), api_key: ApiKey = Depends(get_api_key)):
    return crud.create_user(db, user, api_key.source_name)

@router.post("/edit/{user_id}", response_model=schemas.UserOut)
def edit_user(user_id: int, update: schemas.UserUpdate, db: Session = Depends(get_db), api_key: ApiKey = Depends(get_api_key)):
    user = crud.update_user_status(db, user_id, update.status, api_key.source_name)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/list", response_model=List[schemas.UserOut])
def list_users(
    db: Session = Depends(get_db),
    api_key: ApiKey = Depends(get_api_key),
    status: Optional[str] = None,
    phone_prefix: Optional[str] = None,
    date_from: Optional[datetime] = None,
    date_to: Optional[datetime] = None,
):
    return crud.get_users(db, api_key.source_name, status, phone_prefix, date_from, date_to)
