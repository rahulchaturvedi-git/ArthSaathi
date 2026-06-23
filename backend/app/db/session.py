from typing import Generator
from sqlalchemy.orm import sessionmaker, Session
from app.db.database import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency that yields a database session.
    Closes the session automatically when the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
