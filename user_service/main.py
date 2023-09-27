"""
Main entry point of the User Service application.
This script initializes the FastAPI application and adds routers.
"""

import logging

from fastapi import FastAPI

from config.events import shutdown_event, startup_event
from config.logging_config import configure_logging
from config.middlewares_config import add_middlewares
from config.routers_config import include_routers
from constants.main_constants import APP_DESCRIPTION, APP_TITLE, APP_VERSION

# Initialize logging
configure_logging()
logger = logging.getLogger(__name__)

# Initialize FastAPI
app = FastAPI(title=APP_TITLE, description=APP_DESCRIPTION, version=APP_VERSION)


@app.on_event("startup")
async def on_startup():
    """
    This event is executed on startup.
    """
    await startup_event()


@app.on_event("shutdown")
async def on_shutdown():
    """
    This event is executed on shutdown.
    """
    await shutdown_event()


# Add middlewares
add_middlewares(app)


# Include routers
include_routers(app)
