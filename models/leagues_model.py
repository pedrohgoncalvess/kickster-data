from sqlalchemy import Table, Column, MetaData, Boolean, Integer, Computed, String, Identity, ForeignKey, CHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from typing import List
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Leagues(Base):
    __tablename__ = "leagues"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    country: Mapped[str] = mapped_column(String(15), nullable=False)
    type: Mapped[str] = mapped_column(String(7), nullable=False)
    season: Mapped[int] = mapped_column(Integer, nullable=False)
    start_league: Mapped[int] = mapped_column(Integer, nullable=False)
    end_league: Mapped[int] = mapped_column(Integer, nullable=False)
    logo: Mapped[Optional[str]] = mapped_column(String(250), nullable=False)