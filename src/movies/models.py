from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from src.database import Base

class Base(DeclarativeBase):
    pass

class DVD(Base):
    __tablename__ = "dvds"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    dvdtitle:Mapped[str] = mapped_column(String(50), unique=True,index=True)
    dvdgenre:Mapped[str] = mapped_column(String(50), index=True)
    dvditems:Mapped[int] = mapped_column(index=True)
