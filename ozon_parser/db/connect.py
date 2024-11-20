from typing import Any

from config import config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker

engine = create_async_engine(
    config.postgresql.db_url,
    echo=True,
    max_overflow=0,
    pool_size=5,
)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    id: Any
    __name__: str
    __allow_unmapped__ = True

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


async def get_connection() -> AsyncSession:
    async with async_session() as session:
        yield session
