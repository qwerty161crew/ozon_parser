from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from ozon_parser.config import config

engine = create_async_engine(
    config.postgresql.db_url,
    echo=True,
    max_overflow=0,
    pool_size=5,
)

async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_connection() -> AsyncSession:
    async with async_session() as session:
        return session
