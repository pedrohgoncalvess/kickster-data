from typing import Optional
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from models.declarative_base import Base


class FixturesLineups(Base):
    __tablename__ = "fixtures_lineups"
    __table_args__ = {"schema": "ftd"}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_team: Mapped[int] = mapped_column(ForeignKey("ftd.teams.id"), nullable=False)
    id_fixture: Mapped[int] = mapped_column(ForeignKey("ftd.fixtures.id"), nullable=False)
    id_player: Mapped[int] = mapped_column(ForeignKey("ftd.players.id"), nullable=False)

    type: Mapped[str] = mapped_column(String(5), nullable=False)
    position: Mapped[Optional[str]] = mapped_column(String(1), nullable=True)
    grid: Mapped[str] = mapped_column(String(3), nullable=False)

    fixture_lineup_fk: Mapped["Fixtures"] = relationship(back_populates="fk_fixture_lineup")
    fixture_lineup_team_fk: Mapped["Teams"] = relationship(back_populates="fk_fixture_lineup_team")
    fixture_lineup_player_fk: Mapped["Players"] = relationship(back_populates="fk_fixture_lineup_player")