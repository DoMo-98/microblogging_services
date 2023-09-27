"""
Define database models using SQLAlchemy or another ORM
"""

from datetime import datetime
from typing import Optional


class User:
    """
    User entity
    """

    def __init__(
        self,
        username: str,
        email: str,
        hashed_password: str,
        _id: Optional[int] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self._id = _id
        self.username = username
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = created_at
        self.updated_at = updated_at

    def get_id(self) -> Optional[int]:
        """
        Get user ID
        """
        return self._id

    def set_id(self, _id: int):
        """
        Set user ID
        """
        self._id = _id
