from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.User import User
from services.authService import create_access_token, verify_password, hash_password
from db import get_db
from pydantic import BaseModel

router = APIRouter()

class UserAuth(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(user: UserAuth, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserAuth, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token({"sub": db_user.username})
    return {"access_token": access_token, "token_type": "bearer"}
