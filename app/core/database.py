from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.core.settings import settings

# движок
engine = create_async_engine(
    url=settings.db_url,
    echo=settings.db_echo,
)

# Фабрика сессий
AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False)


# генератор, отдает сессию для подключения к бд, открытия транзакции и взаимодействия
async def get_session_with_db():
    async with AsyncSession() as session:
        yield session
