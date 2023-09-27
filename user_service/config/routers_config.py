"""
Routers configuration
"""

from fastapi import FastAPI

from app.entrypoints.http.routers.user_router import router as user_router
from constants.main_constants import USER_ROUTER_PREFIX, USER_ROUTER_TAGS


def include_routers(app: FastAPI):
    """
    Adds routers to the FastAPI application.
    """
    app.include_router(user_router, prefix=USER_ROUTER_PREFIX, tags=USER_ROUTER_TAGS)
