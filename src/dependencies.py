from fastapi import Depends, Header, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import ApiKey
from sqlalchemy import select

def get_api_key(x_api_key: str = Header(...), db: Session = Depends(get_db)) -> ApiKey:
    stmt = select(ApiKey).where(ApiKey.key == x_api_key)
    api_key = db.scalar(stmt)
    
    if not api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key
