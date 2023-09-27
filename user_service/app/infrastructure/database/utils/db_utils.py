"""
Additional utilities and functions
You could include here any additional database-related utilities or functions that do not fit neatly into the other files, 
such as the logic for initializing the database, e.g.
"""

import logging

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from app.infrastructure.database.config.db_config import engine
from app.infrastructure.database.exceptions.database_exceptions import (
    DatabaseInitializationError,
)

logger = logging.getLogger(__name__)

Base: DeclarativeMeta = declarative_base()


def init_db():
    """
    Initializes the database
    """
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully.")
    except SQLAlchemyError as _e:
        logger.error("Failed to initialize database: %s", _e)
        raise DatabaseInitializationError() from _e
