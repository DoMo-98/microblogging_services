"""
This module contains the events that will be executed on startup and shutdown
"""

from app.infrastructure.database.utils.db_utils import init_db


async def startup_event():
    """
    Initializes the database on startup
    """
    init_db()


async def shutdown_event():
    """
    Closes the database on shutdown
    """
