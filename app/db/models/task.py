from sqlalchemy import Column, String, Integer, Boolean

from app.db.engine import Base, Engine


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(1024))
    is_completed = Column(Boolean, default=False)


Base.metadata.create_all(bind=Engine)
