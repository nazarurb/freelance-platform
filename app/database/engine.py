from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import config

DATABASE_URL = config.DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    from app.database.models import Base
    Base.metadata.create_all(bind=engine)
