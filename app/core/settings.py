from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://user123:user123@localhost:5435/test_api"
    db_echo: bool = False


settings = Settings()
