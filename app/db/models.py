from datetime import datetime
from decimal import Decimal

from db.connect import Base
from sqlalchemy import (DateTime, Enum, Float, ForeignKey, Integer, Numeric,
                        String, UniqueConstraint)
from sqlalchemy.orm import Mapped, mapped_column


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    marketplace: Mapped[str] = mapped_column(String)
    marketplace_identifier: Mapped[str] = mapped_column(Integer, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    full_price: Mapped[int] = mapped_column(Integer, nullable=False)
    sale_price: Mapped[int] = mapped_column(Integer, nullable=False)
    rating: Mapped[Decimal] = mapped_column(Numeric(3, 2), nullable=True)
    seller: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    __table_args__ = (
        UniqueConstraint(
            "marketplace", "marketplace_identifier", name="uq_marketplace_identifier"
        ),
    )

    def __repr__(self):
        return "<{id}-{title}>".format(id=self.id, title=self.title)
