from sqlalchemy.orm import sessionmaker

from app.db.engine import Engine


Session = sessionmaker(bind=Engine)


def get_db():
    with Session() as session:
        yield session
