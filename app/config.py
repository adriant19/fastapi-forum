from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: str
    DB_PASSWORD: str

    class Config:  # read from .env file
        env_file = ".env"


settings = Settings()
