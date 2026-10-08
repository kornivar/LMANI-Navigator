from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database.connection import Base


class Route(Base):
    __tablename__ = "routes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    start_point: Mapped[str] = mapped_column(
        String(1),
        nullable=False,
    )

    finish_point: Mapped[str] = mapped_column(
        String(1),
        nullable=False,
    )

    route: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    distance: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    time: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    traffic: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    actual_time: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    actual_distance: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )