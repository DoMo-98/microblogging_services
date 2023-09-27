"""
User use cases
"""

from app.domain.entities.user_entity import User
from app.domain.interfaces.user_repository import UserRepository
from app.entrypoints.http.schemas.user_schema import UserCreateSchema, UserSchema
from app.infrastructure.mappers.users import entity_schema_mapper
from app.infrastructure.security.interfaces.hashing_strategy import HashingStrategy


def register_user(
    user_schema: UserCreateSchema,
    user_repository: UserRepository,
    hashing_strategy: HashingStrategy,
) -> UserSchema:
    """
    Register a new user
    """
    user_data = user_schema.model_dump()
    user_data["hashed_password"] = hashing_strategy.hash(
        user_data.pop("password")
    )  # TODO: Use literals
    new_user = user_repository.add(User(**user_data))
    return entity_schema_mapper.to_schema(new_user)


# def delete_user(user_id: int, user_repository: UserRepository):
#     """
#     Delete a user
#     """
