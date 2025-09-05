from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    status: str

class UserOut(UserBase):
    id: int
    source_name: str
    status: str
    created_at: datetime

class ApiKeyCreate(BaseModel):
    source_name: str

class ApiKeyOut(BaseModel):
    api_key: str
    source_name: str
