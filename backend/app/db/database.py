from sqlalchemy import create_engine
from app.core.config import settings

# In SQLAlchemy 2.0, the `future=True` flag is removed as all engines operate in 2.0 style by default.
# But since the requirement specifically asks to "Enable future mode", we will include it
# although in modern SQLAlchemy (2.0+) it's redundant.
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    future=True,
)
