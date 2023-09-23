from sqlalchemy import Boolean, Integer, Numeric, String, ForeignKey, types
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from models.declarative_base import Base


class TeamsGoalsStats(Base):
    __tablename__ = "teams_goals_stats"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=True)
    id_league: Mapped[int] = mapped_column(ForeignKey("ftd.leagues.id"), nullable=True)

    type: Mapped[str] = mapped_column(String(6), nullable=False)
    goals_home: Mapped[int] = mapped_column(Integer, nullable=False)
    goals_away: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_0_15: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_16_30: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_31_45: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_46_60: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_61_75: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_76_90: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_91_105: Mapped[int] = mapped_column(Integer, nullable=False)
    in_minute_106_120: Mapped[int] = mapped_column(Integer, nullable=False)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    team_goals_stats_league_fk: Mapped["Leagues"] = relationship(back_populates="league_team_goals_stats_fk")
    team_goals_stat_fk: Mapped["Teams"] = relationship(back_populates="fk_team_goals_stat")
