import uuid

from src import models, schemas
from sqlalchemy.orm import Session


def create_api_key(db: Session, source_name: str):
    api_key = models.ApiKey(key=str(uuid.uuid4()), source_name=source_name)
    db.add(api_key)
    db.commit()
    db.refresh(api_key)
    return api_key

def create_user(db: Session, user: schemas.UserCreate, source_name: str):
    db_user = models.User(**user.model_dump(), source_name=source_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_status(db: Session, user_id: int, status: str, source_name: str):
    user = db.query(models.User).filter(
        models.User.id == user_id, models.User.source_name == source_name
    ).first()
    if user:
        user.status = status
        db.commit()
        db.refresh(user)
    return user

def get_users(db: Session, source_name: str, status=None, phone_prefix=None, date_from=None, date_to=None):
    query = db.query(models.User).filter(models.User.source_name == source_name)
    if status:
        query = query.filter(models.User.status == status)
    if phone_prefix:
        query = query.filter(models.User.phone.startswith(phone_prefix))
    if date_from:
        query = query.filter(models.User.created_at >= date_from)
    if date_to:
        query = query.filter(models.User.created_at <= date_to)
    return query.all()
