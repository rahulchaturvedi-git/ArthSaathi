from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel

class Role(BaseModel):
    """
    Production-grade Role model representing different user roles.
    Example roles: USER, ADMIN, MODERATOR.
    """
    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
