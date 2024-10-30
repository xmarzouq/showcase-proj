from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    url: str = os.environ.get("DATABASE_URL")


settings = Settings()
