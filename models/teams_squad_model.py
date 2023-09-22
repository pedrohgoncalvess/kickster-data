from sqlalchemy import Boolean, Integer, String, ForeignKey, types
from sqlalchemy.orm import Mapped
from sqlalchemy.sql import func
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy.orm import relationship
from models.declarative_base import Base


class TeamsSquad(Base):
    __tablename__ = "teams_squad"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)
    id_player: Mapped[int] = mapped_column(ForeignKey("ftd.players.id"), nullable=False, unique=True)

    shirt_number: Mapped[Optional[int]] = mapped_column(Integer, nullable=False)
    position: Mapped[str] = mapped_column(String(30), nullable=True)
    injured: Mapped[bool] = mapped_column(Boolean, nullable=True)
    updated_at: Mapped[Optional[types.DateTime]] = mapped_column(String(20), nullable=True, default=func.now())

    team_squad_fk: Mapped["Teams"] = relationship(back_populates="fk_team_squad")
    team_squad_player_fk: Mapped["Players"] = relationship(back_populates="fk_player_team_squad")
