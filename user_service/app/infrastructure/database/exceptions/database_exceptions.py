"""
Database exceptions
"""

from app.infrastructure.database.constants.exception_constants import (
    DATABASE_INITIALIZATION_ERROR,
)


class DatabaseInitializationError(Exception):
    """
    Exception raised when the database fails to initialize
    """

    def __init__(self, message: str = DATABASE_INITIALIZATION_ERROR):
        super().__init__(message)
