"""
Database session management
It would contain the logic for creating database sessions
"""

# from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from app.infrastructure.database.config.db_config import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# @contextmanager
def get_db() -> SessionLocal:
    """
    Creates a new database session and closes it after the context is exited
    """
    _db = SessionLocal()
    try:
        yield _db
    finally:
        _db.close()
