from sqlalchemy import Table, Column, MetaData, Boolean, Integer, Computed, String, Identity, ForeignKey, CHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from typing import List
from models.declarative_base import Base
from models.fixtures_stats_model import FixturesStats


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
    team_fixture_stat_fk: Mapped[List["FixturesStats"]] = relationship(back_populates="fixture_stat_team_fk")
    team_player_stat_fk: Mapped[List["PlayersStats"]] = relationship(back_populates="player_stat_team_fk")

    fk_team_squad: Mapped[List["TeamsSquad"]] = relationship(back_populates="team_squad_fk")
    fk_team_fixture_event: Mapped[List["FixturesEvents"]] = relationship(back_populates="fixture_event_team_fk")
    fk_team_fixture_stat: Mapped[List["TeamsFixturesStats"]] = relationship(back_populates="team_fixture_stat_fk")
    fk_team_cards_stat: Mapped[List["TeamsCardsStats"]] = relationship(back_populates="team_cards_stat_fk")
    fk_team_goals_stat: Mapped[List["TeamsGoalsStats"]] = relationship(back_populates="team_goals_stat_fk")