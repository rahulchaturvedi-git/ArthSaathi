"""
Application settings — loaded once from environment / .env file.

Uses Pydantic Settings v2 with a singleton pattern so every module
imports the same validated ``Settings`` instance.
"""

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# Resolve .env relative to the *backend* package root
# (backend/.env), regardless of where the process is started.
_ENV_FILE: Path = Path(__file__).resolve().parents[2] / ".env"


class Settings(BaseSettings):
    """Central, validated configuration for the entire application."""

    model_config = SettingsConfigDict(
        env_file=str(_ENV_FILE),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # ── Application ──────────────────────────────────────────────
    APP_NAME: str = "ArthSaathi"

    # ── Database (PostgreSQL) ────────────────────────────────────
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "arthsaathi"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = ""

    # ── Redis ────────────────────────────────────────────────────
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # ── JWT / Auth ───────────────────────────────────────────────
    JWT_SECRET_KEY: str  # required — no default, forces explicit config
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ── Computed helpers (not read from env) ─────────────────────
    @property
    def database_url(self) -> str:
        """Async-compatible PostgreSQL DSN."""
        return (
            f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached (singleton) ``Settings`` instance."""
    return Settings()


# Module-level convenience alias
settings: Settings = get_settings()
