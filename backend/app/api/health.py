from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.db.session import get_db

router = APIRouter()

@router.get("/health/db", tags=["Health"])
async def health_check_db(db: Session = Depends(get_db)):
    """
    Check if the database is reachable.
    """
    try:
        # Execute a simple SELECT 1 to verify database connectivity.
        db.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }
    except Exception as e:
        # If the query fails, return a 503 Service Unavailable error.
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "status": "unhealthy",
                "database": "disconnected",
                "error": str(e)
            }
        )
