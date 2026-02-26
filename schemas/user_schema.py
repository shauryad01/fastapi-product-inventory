from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id: int
    email: str
    created_on: datetime
    last_login: datetime | None = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token:str
    token_type:str