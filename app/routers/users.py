from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.User import User
from app.schemas.User import UserSchema, UserSchemaCreate
from app.dependencies.database import get_db

router = APIRouter(prefix='/users', tags=['users'])


@router.get('/', response_model=List[UserSchema])
def users(db: Session = Depends(get_db)):
    return db.query(User).all()


@router.get('/{user_id}', response_model=UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = User.get_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')
    return db_user


@router.post('/', response_model=UserSchema)
def create_user(user: UserSchemaCreate, db: Session = Depends(get_db)):
    db_user = User.get_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email already registered')

    try:
        new_user = User.create(db, user)
    except HTTPException:
        raise HTTPException(status_code=500, detail='Something wrong :(')
    return new_user
