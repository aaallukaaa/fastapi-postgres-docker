from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.config.config import pg_settings


def get_engine(pg_settings=pg_settings):
    url = pg_settings.PG_URL
    engine = create_engine(url, echo=False)
    return engine


Engine = get_engine()
Base = declarative_base()
