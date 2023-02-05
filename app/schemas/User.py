from pydantic import BaseModel


class UserSchemaBase(BaseModel):
    email: str
    name: str


class UserSchemaCreate(UserSchemaBase):
    password: str


class UserSchema(UserSchemaBase):
    id: int
    name: str

    class Config:
        orm_mode = True
