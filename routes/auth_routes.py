from fastapi import APIRouter, Depends, HTTPException
from database.connection import session
from database.user_model import User
from schemas.user_schema import UserCreate, UserLogin
from sqlalchemy.orm import Session
from utils.auth import hash_password, verify_password, create_access_token
from datetime import datetime
import config


router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db=session()
    yield db
    db.close()

@router.get("/test")
def auth_test():
    return "auth success"

@router.post("/signup")
def signup(user:UserCreate, db:Session=Depends(get_db)):
    existing = db.query(User).filter(user.email==User.email).first()
    if existing:
        raise HTTPException(status_code=400, detail= "User already exists")
    
    now = datetime.now()

    hashed_pwd = hash_password(user.password)
    newUser = User(
        email=user.email,
        password=hashed_pwd
    )

    db.add(newUser)
    db.commit()
    return{"message":"User created"}


@router.post("/login")
def login(user:UserLogin, db:Session=Depends(get_db)):
    in_db = db.query(User).filter(User.email==user.email).first()
    if not in_db:
        raise HTTPException(status_code=400, detail = "Invalid Email ID")
    
    if not verify_password(user.password, in_db.password):
        raise HTTPException(status_code=400, detail = "Invalid Password")
        
    # token = create_access_token({"sub":existing.email})
    token = create_access_token()
    in_db.last_login = datetime.now()
    config.current_u_id = in_db.id
    db.commit()
    print(config.current_u_id)
    return {"access_token": token, "token_type": "bearer"}

