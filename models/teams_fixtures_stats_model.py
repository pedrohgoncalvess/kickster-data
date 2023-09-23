from sqlalchemy import Integer, Numeric, String, ForeignKey, types
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from models.declarative_base import Base


class TeamsFixturesStats(Base):
    __tablename__ = "teams_fixtures_stats"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=True)
    id_league: Mapped[int] = mapped_column(ForeignKey("ftd.leagues.id"), nullable=True)

    fixtures_home: Mapped[int] = mapped_column(Integer, nullable=False)
    fixtures_away: Mapped[int] = mapped_column(Integer, nullable=False)
    wins_home: Mapped[int] = mapped_column(Integer, nullable=False)
    wins_away: Mapped[int] = mapped_column(Integer, nullable=False)
    draws_home: Mapped[int] = mapped_column(Integer, nullable=False)
    draws_away: Mapped[float] = mapped_column(Numeric, nullable=False)
    loses_home: Mapped[int] = mapped_column(Integer, nullable=False)
    loses_away: Mapped[int] = mapped_column(Integer, nullable=False)
    clean_sheets_home: Mapped[int] = mapped_column(Integer, nullable=False)
    clean_sheets_away: Mapped[int] = mapped_column(Integer, nullable=False)
    not_scored_home: Mapped[int] = mapped_column(Integer, nullable=False)
    not_scored_away: Mapped[int] = mapped_column(Integer, nullable=False)
    max_wins_streak: Mapped[int] = mapped_column(Integer, nullable=False)
    max_draws_streak: Mapped[int] = mapped_column(Integer, nullable=False)
    max_loses_streak: Mapped[int] = mapped_column(Integer, nullable=False)
    better_win_home: Mapped[int] = mapped_column(Integer, nullable=False)
    worst_lose_home: Mapped[int] = mapped_column(Integer, nullable=False)
    better_win_away: Mapped[int] = mapped_column(Integer, nullable=False)
    worst_lose_away: Mapped[int] = mapped_column(Integer, nullable=False)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    team_fixture_stat_league_fk: Mapped["Leagues"] = relationship(back_populates="league_team_fixture_stat_fk")
    team_fixture_stat_fk: Mapped["Teams"] = relationship(back_populates="fk_team_fixture_stat")
