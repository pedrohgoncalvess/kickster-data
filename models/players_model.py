from sqlalchemy import Numeric, Boolean, Integer, String, ForeignKey
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

    name: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    last_name: Mapped[Optional[str]] = mapped_column(String(40), nullable=True)
    date_of_birth: Mapped[Optional[types.Date]] = mapped_column(String(20), nullable=True)

    nationality: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    height: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    weight: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    image: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)

    fk_player_stat: Mapped[List["PlayersStats"]] = relationship(back_populates="player_stat_fk")
    fk_player_team_squad: Mapped[List["TeamsSquad"]] = relationship(back_populates="team_squad_player_fk")
    fk_fixture_event_principal_player = relationship("FixturesEvents", back_populates="fixture_event_principal_player_fk", foreign_keys="[FixturesEvents.id_player_principal]")
    fk_fixture_event_assist_player = relationship("FixturesEvents", back_populates="fixture_event_assist_player_fk", foreign_keys="[FixturesEvents.id_player_assist]")