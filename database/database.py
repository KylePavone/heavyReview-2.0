from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

import settings


engine = create_async_engine(settings.DB_URL, future=True, echo=True)
# execution_options(autocommit=True)
session_options = {
    'autocommit': True
}
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


