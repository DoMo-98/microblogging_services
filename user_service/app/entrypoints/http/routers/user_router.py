"""
User controller
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.application.use_cases import user_service
from app.entrypoints.http.schemas.user_schema import UserCreateSchema, UserSchema
from app.infrastructure.database.session.db_session import get_db
from app.infrastructure.repositories.user_repository import SqlAlchemyUserRepository
from app.infrastructure.security.implementations.bcrypt_hashing import BcryptHashing

router = APIRouter()


@router.post("/", response_model=UserSchema, status_code=201)
def add_user(user: UserCreateSchema, db_session: Session = Depends(get_db)):
    """
    Add a new user
    """
    try:
        return user_service.register_user(
            user, SqlAlchemyUserRepository(db_session), BcryptHashing()
        )
    except Exception as _e:
        raise HTTPException(status_code=400, detail=str(_e)) from _e
