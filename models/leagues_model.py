from sqlalchemy import Table, Column, MetaData, Boolean, Integer, Computed, String, Identity, ForeignKey, CHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from typing import List
from models.declarative_base import Base
from models.players_stats_model import PlayersStats
from models.teams_fixtures_stats_model import TeamsFixturesStats
from models.teams_cards_stats_model import TeamsCardsStats
from models.teams_goals_stats_model import TeamsGoalsStats


class Leagues(Base):
    __tablename__ = "leagues"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_league: Mapped[int] = mapped_column(Integer, nullable=False)

    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    country: Mapped[str] = mapped_column(String(15), nullable=False)
    type: Mapped[str] = mapped_column(String(7), nullable=False)
    season: Mapped[int] = mapped_column(Integer, nullable=False)
    start_league: Mapped[int] = mapped_column(Integer, nullable=False)
    end_league: Mapped[int] = mapped_column(Integer, nullable=False)
    logo: Mapped[Optional[str]] = mapped_column(String(250), nullable=False)

    league_fixture: Mapped[List["Fixtures"]] = relationship(back_populates="fixture_league")
    league_player_stat_fk: Mapped[List["PlayersStats"]] = relationship(back_populates="player_stat_league_fk")
    league_team_fixture_stat_fk: Mapped[List["TeamsFixturesStats"]] = relationship(back_populates="team_fixture_stat_league_fk")
    league_team_cards_stats_fk: Mapped[List["TeamsCardsStats"]] = relationship(back_populates="team_cards_stats_league_fk")
    league_team_goals_stats_fk: Mapped[List["TeamsGoalsStats"]] = relationship(back_populates="team_goals_stats_league_fk")

