import os

from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()


class AppSettings(BaseSettings):
    APP_VERSION: str = os.getenv('APP_VERSION')
    APP_NAME: str = os.getenv('APP_NAME')


class PostgresSettings(BaseSettings):
    PG_USER: str = os.getenv('PG_USER', 'postgres')
    PG_PASSWORD: str = os.getenv('PG_PASSWORD', 'postgres')
    PG_HOST: str = os.getenv('PG_HOST', 'localhost')
    PG_PORT: int = os.getenv('PG_PORT', 5432)
    PG_DB_NAME: str = os.getenv('PG_DB_NAME', 'postgres')
    PG_URL: str = f'postgresql+psycopg2://' \
                  f'{PG_USER}:' \
                  f'{PG_PASSWORD}@' \
                  f'{PG_HOST}:' \
                  f'{PG_PORT}/' \
                  f'{PG_DB_NAME}'


app_settings = AppSettings()
pg_settings = PostgresSettings()
