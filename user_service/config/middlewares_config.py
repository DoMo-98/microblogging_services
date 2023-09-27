"""
This is the main middlewares file, where you can add middlewares to the FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from constants.main_constants import ALLOWED_HOSTS


def add_middlewares(app: FastAPI):
    """
    Adds middlewares to the FastAPI application.
    """

    # Add TrustedHostMiddleware
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=ALLOWED_HOSTS)
