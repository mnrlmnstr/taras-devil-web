from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.User import User
from app.schemas.User import UserSchema, UserCreate
from app.dependencies.database import get_db

router = APIRouter(prefix='/users', tags=["users"])


@router.get("/", response_model=List[UserSchema])
def users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.post("/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    fake_hashed_password = user.password + "notreallyhashed"
    new_user = User(email=user.email, name=user.name, hashed_password=fake_hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
