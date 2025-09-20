# alembic/env.py
import os
import sys
from pathlib import Path
from logging.config import fileConfig
from urllib.parse import quote_plus

from alembic import context
from sqlalchemy import engine_from_config, pool
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parents[2].resolve()
sys.path.insert(0, str(PROJECT_ROOT))

config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

sens_path = PROJECT_ROOT / "sens.env"
if sens_path.exists():
    # override=True so local dev can intentionally override shell env
    load_dotenv(sens_path, override=True)

db_url = os.getenv("DATABASE_URL")

if not db_url:
    # Fallback for local development if DATABASE_URL isn't set
    user = os.getenv("DB_USER", "")
    raw_pw = os.getenv("DB_PASSWORD", "")
    password = quote_plus(raw_pw) if raw_pw else ""
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432") or "5432"
    db_name = os.getenv("DB_NAME", "fitness_app_db")

    # For psycopg2-binary you can use plain "postgresql://"
    # ("postgresql+psycopg2://" also works)
    if user and password:
        auth = f"{user}:{password}@"
    elif user:
        auth = f"{user}@"
    else:
        auth = ""

    db_url = f"postgresql://{auth}{host}:{port}/{db_name}"

# Escape % so ConfigParser doesn't treat them as interpolation placeholders
escaped_url = db_url.replace("%", "%%")
config.set_main_option("sqlalchemy.url", escaped_url)

from application.database import Base  # noqa: E402
from application.models import (      # noqa: E402, adjust if your models live elsewhere
    User,
    workouts,
    workout_sections,
    workoutRoutine,
    UserWorkoutRequest,
    UserProfile,
)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    if not url:
        raise RuntimeError("sqlalchemy.url is not configured for offline migrations")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section) or {},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
