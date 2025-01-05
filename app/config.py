from pathlib import Path, PurePath

from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    ROOT_DIR: Path = Path(__file__).resolve().parent.parent


app_settings = AppSettings()


class DBSettings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    @property
    def database_url(self):
        return f'''postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'''

    model_config = SettingsConfigDict(
        env_file=app_settings.ROOT_DIR / ".env"
    )


db_settings = DBSettings()

