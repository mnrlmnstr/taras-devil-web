from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
    name: str


class UserSchema(UserBase):
    id: int

    class Config:
        orm_mode = True
