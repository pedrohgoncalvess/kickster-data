from sqlalchemy import Table, Column, MetaData, Boolean, Integer, Computed, String, Identity, ForeignKey, CHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional, List
from sqlalchemy.orm import relationship
from models.declarative_base import Base
from sqlalchemy import types


class Players(Base):
    __tablename__ = "players"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[Optional[str]] = mapped_column(String(150), nullable=False)
    first_name: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)
    date_of_birth: Mapped[Optional[types.Date]] = mapped_column(String(40), nullable=True)

    nationality: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    height: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    weight: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    image: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
