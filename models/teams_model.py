from sqlalchemy import Table, Column, MetaData, Boolean, Integer, Computed, String, Identity, ForeignKey, CHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from typing import List
from models.declarative_base import Base


class Teams(Base):
    __tablename__ = "teams"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    id_stadium: Mapped[Optional[int]] = mapped_column(ForeignKey("ftd.stadiums.id"), nullable=True)

    code: Mapped[Optional[str]] = mapped_column(String(3), nullable=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    country: Mapped[str] = mapped_column(String(15), nullable=False)
    logo: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
    founded: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    national: Mapped[bool] = mapped_column(Boolean, nullable=False)

    home_stadium: Mapped["Stadiums"] = relationship(back_populates="stadium_team")
    fixture_team_home = relationship("Fixtures", back_populates="team_home", foreign_keys="[Fixtures.id_team_home]")
    fixture_team_away = relationship("Fixtures", back_populates="team_away", foreign_keys="[Fixtures.id_team_away]")
