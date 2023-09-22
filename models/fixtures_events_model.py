from sqlalchemy import Boolean, Integer, String, ForeignKey, types
from sqlalchemy.orm import Mapped
from sqlalchemy.sql import func
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from models.declarative_base import Base


class FixturesEvents(Base):
    __tablename__ = "fixtures_events"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)
    id_fixture: Mapped[int] = mapped_column(ForeignKey("ftd.fixtures.id"), nullable=False)
    id_player_principal: Mapped[int] = mapped_column(ForeignKey("ftd.players.id"), nullable=False)
    id_player_assist: Mapped[Optional[int]] = mapped_column(ForeignKey("ftd.players.id"), nullable=True)

    time: Mapped[int] = mapped_column(Integer, nullable=False)
    type_event: Mapped[str] = mapped_column(String(20), nullable=False)
    detail: Mapped[str] = mapped_column(String(30), nullable=False)
    comments: Mapped[str] = mapped_column(String(30), nullable=False)

    fixture_event_fk: Mapped["Fixtures"] = relationship(back_populates="fk_fixture_event")
    fixture_event_team_fk: Mapped["Teams"] = relationship(back_populates="fk_team_fixture_event")
    fixture_event_principal_player_fk = relationship("Players", back_populates="fk_fixture_event_principal_player", foreign_keys="[FixturesEvents.id_player_principal]")
    fixture_event_assist_player_fk = relationship("Players", back_populates="fk_fixture_event_assist_player", foreign_keys="[FixturesEvents.id_player_assist]")
