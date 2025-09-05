from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from src.database import Base


class ApiKey(Base):
    __tablename__ = "api_keys"
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True, nullable=False)
    source_name = Column(String, nullable=False)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    source_name = Column(String, nullable=False)
    status = Column(String, default="NEW")
    created_at = Column(DateTime, default=datetime.now)
