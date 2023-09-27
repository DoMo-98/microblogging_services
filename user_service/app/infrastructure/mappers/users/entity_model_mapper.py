"""
User entity to model mapper
"""

from app.domain.entities.user_entity import User
from app.infrastructure.database.models.user_model import UserModel


def to_entity(user_model: UserModel) -> User:
    """
    Convert a user model to a user entity
    """
    return User(
        _id=user_model.id,
        username=user_model.username,
        email=user_model.email,
        hashed_password=user_model.hashed_password,
        created_at=user_model.created_at,
        updated_at=user_model.updated_at,
    )


def to_model(user: User) -> UserModel:
    """
    Convert a user entity to a user model
    """
    user_model = UserModel(
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )
    if user.get_id() is not None:
        user_model.id = user.get_id()
    return user_model
