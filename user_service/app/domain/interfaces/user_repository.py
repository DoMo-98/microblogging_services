"""
Service interfaces
"""
from abc import ABC, abstractmethod

from app.domain.entities.user_entity import User


class UserRepository(ABC):
    """
    User repository interface
    """

    @abstractmethod
    def add(self, user: User) -> User:
        """
        Add a new user
        """
