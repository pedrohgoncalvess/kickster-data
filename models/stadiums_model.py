from sqlalchemy import Table, Column, MetaData, Boolean, Integer, Computed, String, Identity, ForeignKey, CHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional, List
from sqlalchemy.orm import relationship
from models.declarative_base import Base


class Stadiums(Base):
    __tablename__ = "stadiums"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    teams: Mapped[List["Teams"]] = relationship(back_populates="stadiums")

    name: Mapped[Optional[str]] = mapped_column(String(150), nullable=False, unique=True)
    state: Mapped[str] = mapped_column(String(40), nullable=False)
    city: Mapped[Optional[str]] = mapped_column(String(50), nullable=False)
    address: Mapped[Optional[str]] = mapped_column(String(250), nullable=False)
    capacity: Mapped[Optional[int]] = mapped_column(Integer, nullable=False)
    surface: Mapped[Optional[str]] = mapped_column(String(30), nullable=False)
    image: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
