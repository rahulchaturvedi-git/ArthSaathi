import logging
from contextlib import asynccontextmanager
from typing import Any
from app.db.base import Base
from app.db.database import engine
from fastapi import FastAPI
from app.core.config import settings
from app.api.health import router as health_router
import app.models

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
    """
    Application lifespan events.

    Replaces legacy @app.on_event("startup") and @app.on_event("shutdown").
    """
    logger.info(f"Starting up {settings.APP_NAME}...")
    # Add startup logic here (e.g., connect to database, redis, etc.)
    
    Base.metadata.create_all(bind=engine)

    yield
    
    logger.info(f"Shutting down {settings.APP_NAME}...")
    # Add shutdown logic here (e.g., disconnect from database, redis, etc.)


def create_app() -> FastAPI:
    """
    Application factory.
    """
    app = FastAPI(
        title=settings.APP_NAME,
        lifespan=lifespan,
    )

    @app.get("/health", tags=["Health"])
    async def health_check() -> dict[str, str]:
        """
        Simple health check endpoint.
        """
        return {"status": "healthy"}

    # Include routers here
    app.include_router(health_router)

    return app


app = create_app()
