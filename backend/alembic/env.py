# alembic/env.py
import os
import sys
from pathlib import Path
from logging.config import fileConfig
from urllib.parse import quote_plus

from alembic import context
from sqlalchemy import engine_from_config, pool
from dotenv import load_dotenv

#Paths / config
PROJECT_ROOT = Path(__file__).parents[2].resolve()
sys.path.insert(0, str(PROJECT_ROOT))

config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

#Detect production on Fly (Fly sets FLY_APP_NAME)
IN_FLY = bool(os.getenv("FLY_APP_NAME"))

#Load sens.env ONLY in local/dev and NEVER override real env vars
sens_path = PROJECT_ROOT / "sens.env"
if not IN_FLY and sens_path.exists():
    load_dotenv(sens_path, override=False)

#Pick the DB URL
db_url = (
    os.getenv("DATABASE_URL")
    or os.getenv("SQLALCHEMY_DATABASE_URL")
    or os.getenv("DB_URL")
)

#In production, require DATABASE_URL. In dev, allow a localhost fallback.
if not db_url:
    if IN_FLY:
        raise RuntimeError("DATABASE_URL not set (production)")
    # Fallback for local development
    user = os.getenv("DB_USER", "")
    raw_pw = os.getenv("DB_PASSWORD", "")
    password = quote_plus(raw_pw) if raw_pw else ""
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432") or "5432"
    db_name = os.getenv("DB_NAME", "fitness_app_db")

    if user and password:
        auth = f"{user}:{password}@"
    elif user:
        auth = f"{user}@"
    else:
        auth = ""
    # psycopg2/SQLAlchemy both accept plain "postgresql://"
    db_url = f"postgresql://{auth}{host}:{port}/{db_name}"

#Neon safety: ensure TLS
if "neon.tech" in db_url and "sslmode=" not in db_url:
    db_url += ("&" if "?" in db_url else "?") + "sslmode=require"

#Escape % so ConfigParser doesn't interpolate
escaped_url = db_url.replace("%", "%%")
config.set_main_option("sqlalchemy.url", escaped_url)

#Import models' metadata
from application.database import Base  # noqa: E402
from application.models import (       # noqa: E402
    User,
    workouts,
    workout_sections,
    workoutRoutine,
    UserWorkoutRequest,
    UserProfile,
)

target_metadata = Base.metadata

#Alembic runners
def run_migrations_offline() -> None:
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
