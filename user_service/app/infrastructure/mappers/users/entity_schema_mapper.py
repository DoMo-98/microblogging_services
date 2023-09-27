"""
User Entity Schema Mapper
"""

from app.domain.entities.user_entity import User
from app.entrypoints.http.schemas.user_schema import UserSchema


def to_entity(user_schema: UserSchema) -> User:
    """
    Convert a user schema to a user entity
    """
    return User(
        _id=user_schema.get_id(),
        username=user_schema.username,
        email=user_schema.email,
        hashed_password=user_schema.hashed_password,
        created_at=user_schema.created_at,
        updated_at=user_schema.updated_at,
    )


def to_schema(user: User) -> UserSchema:
    """
    Convert a user entity to a user schema
    """
    user_schema = UserSchema(
        id=user.get_id(),
        username=user.username,
        email=user.email,
        hashed_password=user.hashed_password,
        created_at=user.created_at,
        updated_at=user.updated_at,
    )
    return user_schema
