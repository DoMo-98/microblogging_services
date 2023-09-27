"""
Defines Pydantic models for data validation and serialization
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    """
    User base schema
    """

    username: str
    email: str


class UserCreateSchema(UserBaseSchema):
    """
    User create schema
    """

    password: str


class UserUpdateSchema(UserBaseSchema):
    """
    User update schema
    """

    username: Optional[str]
    email: Optional[str]


class UserInDBSchema(UserBaseSchema):
    """
    User in database schema
    """

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        """
        Config
        """

        from_attributes = True


class UserSchema(UserInDBSchema):
    """
    User response schema
    """
