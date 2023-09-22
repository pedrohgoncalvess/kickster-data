from sqlalchemy import Table, Column, MetaData, Boolean, Integer, Computed, String, Identity, ForeignKey, CHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional, List
from sqlalchemy.orm import relationship
from models.declarative_base import Base
from sqlalchemy import types


class FixturesStats(Base):
    __tablename__ = "fixtures_stats"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_fixture: Mapped[int] = mapped_column(ForeignKey("ftd.fixtures.id"), nullable=False)
    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)

    id_coach: Mapped[int] = mapped_column(Integer, nullable=False)
    formation: Mapped[Optional[str]] = mapped_column(String(10), nullable=False)
    shots_on_goal: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_off_goal: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_blocked: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_inside_box: Mapped[int] = mapped_column(Integer, nullable=False)
    shots_offside_box: Mapped[int] = mapped_column(Integer, nullable=False)
    fouls: Mapped[int] = mapped_column(Integer, nullable=False)
    corners: Mapped[int] = mapped_column(Integer, nullable=False)
    offsides: Mapped[int] = mapped_column(Integer, nullable=False)
    possession: Mapped[int] = mapped_column(Integer, nullable=False)
    yellow_cards: Mapped[int] = mapped_column(Integer, nullable=False)
    red_cards: Mapped[int] = mapped_column(Integer, nullable=False)
    goalkeeper_saves: Mapped[int] = mapped_column(Integer, nullable=False)
    total_passes: Mapped[int] = mapped_column(Integer, nullable=False)
    accurate_passes: Mapped[int] = mapped_column(Integer, nullable=False)
    expected_goals: Mapped[int] = mapped_column(Integer, nullable=False)

    fixture_fk: Mapped["Fixtures"] = relationship(back_populates="fixture_stat_fk")
    fixture_stat_team_fk: Mapped["Teams"] = relationship(back_populates="team_fixture_stat_fk")
