from datetime import datetime

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseModel

class User(BaseModel):
    """
    Production-grade User model representing application users.
    """
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)

    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)

    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
