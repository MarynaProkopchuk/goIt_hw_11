from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), index=True)
    surname: Mapped[str] = mapped_column(String(50), index=True)
    email: Mapped[str] = mapped_column(String(50), index=True, unique=True)
    phone: Mapped[str] = mapped_column(String(10), unique=True)
    birthday: Mapped[Date] = mapped_column(Date)
