import uuid
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from app.models.base_model import BaseModel

class UserRole(BaseModel):
    """
    Production-grade UserRole model representing the many-to-many relationship
    between users and roles.
    """
    __tablename__ = "user_roles"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
    
    role_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), 
        ForeignKey("roles.id", ondelete="CASCADE"), 
        nullable=False, 
        index=True
    )
