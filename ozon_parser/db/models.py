from decimal import Decimal
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import TIMESTAMP
from sqlalchemy import Enum as En
from sqlalchemy import func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class StateEnum(Enum):
    RUNNING: str = "running"
    COMPLETED: str = "completed"
    FAIL: str = "fail"


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "Task"
    id: Mapped[UUID] = mapped_column(
        "id",
        UUID(as_uuid=True),
        default=uuid4,
        primary_key=True,
        server_default=text("gen_random_uuid()"),
        unique=True,
        nullable=False,
        index=True,
    )

    task_id: Mapped[UUID] = mapped_column(
        "task_id",
        UUID(as_uuid=True),
        default=uuid4,
        unique=True,
        nullable=False,
    )
    state: Mapped[StateEnum] = mapped_column(En(StateEnum), nullable=False)
    message: Mapped[str] = mapped_column(nullable=True)


class Product(Base):
    __tablename__ = "Product"
    id: Mapped[UUID] = mapped_column(
        "id",
        UUID(as_uuid=True),
        default=uuid4,
        primary_key=True,
        server_default=text("gen_random_uuid()"),
        unique=True,
        nullable=False,
        index=True,
    )
    ozon_id: Mapped[int] = mapped_column(unique=True)
    title: Mapped[str] = mapped_column()
    full_price: Mapped[Decimal] = mapped_column()
    sale_price: Mapped[Decimal] = mapped_column()
    rating: Mapped[Decimal] = mapped_column()
    saller: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
