"""
Implementation of the user repository using SQLAlchemy
"""

from sqlalchemy.orm import Session

from app.domain.entities.user_entity import User
from app.domain.interfaces.user_repository import UserRepository
from app.infrastructure.mappers.users import entity_model_mapper


class SqlAlchemyUserRepository(UserRepository):
    """
    User repository implementation using SQLAlchemy
    """

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def add(self, user: User) -> User:
        """
        Add a user to the database
        """
        user_model = entity_model_mapper.to_model(user)
        self.db_session.add(user_model)
        self.db_session.commit()
        self.db_session.refresh(user_model)
        return entity_model_mapper.to_entity(user_model)
