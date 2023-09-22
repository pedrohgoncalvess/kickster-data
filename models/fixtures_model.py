from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional, List
from sqlalchemy.orm import relationship
from models.declarative_base import Base
from sqlalchemy import types
from models.leagues_model import Leagues
from models.stadiums_model import Stadiums


class Fixtures(Base):
    __tablename__ = "fixtures"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    id_stadium: Mapped[Optional[int]] = mapped_column(ForeignKey("ftd.stadiums.id"), nullable=True)
    id_league: Mapped[int] = mapped_column(ForeignKey("ftd.leagues.id"), nullable=False)
    id_team_home: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)
    id_team_away: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)

    start_at: Mapped[types.DateTime] = mapped_column(String(20), nullable=False)
    result: Mapped[str] = mapped_column(String(11), nullable=False)
    round: Mapped[str] = mapped_column(String(30), nullable=False)
    referee: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    data_stats: Mapped[str] = mapped_column(String(10), nullable=False, default='waiting')
    data_events: Mapped[str] = mapped_column(String(10), nullable=False, default='waiting')
    data_lineups: Mapped[str] = mapped_column(String(10), nullable=False, default='waiting')

    team_home = relationship("Teams", back_populates="fixture_team_home", foreign_keys="[Fixtures.id_team_home]")
    team_away = relationship("Teams", back_populates="fixture_team_away", foreign_keys="[Fixtures.id_team_away]")
    fixture_league: Mapped["Leagues"] = relationship(back_populates="league_fixture")
    fixture_stadium: Mapped["Stadiums"] = relationship(back_populates="stadium_fixture")
    fixture_stat_fk: Mapped[List["FixturesStats"]] = relationship(back_populates="fixture_fk")
    fk_fixture_event: Mapped[List["FixturesEvents"]] = relationship(back_populates="fixture_event_fk")
