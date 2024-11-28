from enum import Enum
from uuid import uuid4

from sqlalchemy import TIMESTAMP, func, text
from sqlalchemy import Enum as En
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class StateEnum:
    RUNNING: str = "running"
    COMPLETED: str = "completed"
    FAIL: str = "fail"


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "Task"
    id: Mapped[UUID] = mapped_column(
        "uuid",
        UUID(as_uuid=True),
        default=uuid4,
        primary_key=True,
        server_default=text("gen_random_uuid()"),
        unique=True,
        nullable=False,
        index=True,
    )

    task_id: Mapped[UUID] = mapped_column(unique=True)
    state: Mapped[StateEnum] = mapped_column(En(StateEnum), nullable=False)
    message: Mapped[str] = mapped_column(nullable=True)
