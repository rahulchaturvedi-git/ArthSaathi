import uuid
from datetime import datetime, timezone

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base

def utc_now() -> datetime:
    return datetime.now(timezone.utc)

class BaseModel(Base):
    """
    Abstract base model that provides:
    - id: UUID4 primary key
    - created_at: UTC timestamp, automatically populated on creation
    - updated_at: UTC timestamp, automatically updated on modification
    """
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        primary_key=True, 
        default=uuid.uuid4, 
        index=True
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=utc_now, 
        nullable=False
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=utc_now, 
        onupdate=utc_now, 
        nullable=False
    )
