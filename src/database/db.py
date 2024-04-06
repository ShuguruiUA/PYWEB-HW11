import contextlib
import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from src.conf.config import config

load_dotenv()


class DBSessionManager:
    def __init__(self, url: str):
        self._engine: AsyncEngine | None = create_async_engine(url)
        self._session_maker: async_sessionmaker = async_sessionmaker(autoflush=False, autocommit=False,
                                                                     bind=self._engine)

    DB_URL = os.environ.get('SQLALCHEMY_DB')

    @contextlib.asynccontextmanager
    async def session(self):
        if self._session_maker is None:
            raise Exception("Session is not initialized")
        session = self._session_maker()
        try:
            yield session
        except:
            await session.rollback()
        finally:
            await session.close()


session_manager = DBSessionManager(config.DB_URL)


async def get_db():
    async with session_manager.session() as session:
        return session
