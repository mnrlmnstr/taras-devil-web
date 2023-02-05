from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, Session

from app.schemas.User import UserSchemaCreate
from app.dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    hashed_password: Mapped[str] = mapped_column(String)

    @classmethod
    def get_by_id(cls, db: Session, user_id: int):
        return db.query(cls).filter(cls.id == user_id).first()

    @classmethod
    def get_by_email(cls, db: Session, email: str):
        return db.query(cls).filter(cls.email == email).first()

    @classmethod
    def create(cls, db: Session, user: UserSchemaCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        new_user = User(email=user.email, name=user.name, hashed_password=fake_hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    