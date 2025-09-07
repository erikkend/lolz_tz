import uuid

from src import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy import select, update


def create_api_key(db_session: Session, source_name: str):
    api_key = models.ApiKey(key=str(uuid.uuid4()), source_name=source_name)
    db_session.add(api_key)
    db_session.commit()
    db_session.refresh(api_key)
    
    return api_key

def create_user(db_session: Session, user: schemas.UserCreate, source_name: str):
    db_user = models.User(**user.model_dump(), source_name=source_name)
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return db_user

def update_user_status(db_session: Session, user_id: int, status: str, source_name: str):
    stmt = (
        update(models.User)
        .where(models.User.id == user_id, models.User.source_name == source_name)
        .values(status=status)
    )
    db_session.execute(stmt)
    db_session.commit()
    
    stmt = select(models.User).where(
        models.User.id == user_id, 
        models.User.source_name == source_name
    )
    return db_session.scalar(stmt)

def get_users(db_session: Session, source_name: str, status=None, phone_prefix=None, date_from=None, date_to=None):
    stmt = select(models.User).where(models.User.source_name == source_name)
    
    if status:
        stmt = stmt.where(models.User.status == status)
    if phone_prefix:
        stmt = stmt.where(models.User.phone.startswith(phone_prefix))
    if date_from:
        stmt = stmt.where(models.User.created_at >= date_from)
    if date_to:
        stmt = stmt.where(models.User.created_at <= date_to)
    
    return db_session.scalars(stmt).all()
