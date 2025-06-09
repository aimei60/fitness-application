import os, sys
from pathlib import Path
from logging.config import fileConfig
from urllib.parse import quote_plus

from alembic import context
from sqlalchemy import engine_from_config, pool
from dotenv import load_dotenv

# enables import backend.application.database.
PROJECT_ROOT = Path(__file__).parents[2].resolve()
sys.path.insert(0, str(PROJECT_ROOT))

# load sens.env and override any existing environment variables 
load_dotenv(PROJECT_ROOT / "sens.env", override=True)

# Loads alembic.ini and configures Python’s logging to follow what's declared there.
config = context.config
if config.config_file_name:
    fileConfig(config.config_file_name)

# build the raw DATABASE_URL 
user = os.getenv("DB_USER", "")
raw_pw = os.getenv("DB_PASSWORD", "")
password = quote_plus(raw_pw)
host = os.getenv("DB_HOST", "localhost")
port = os.getenv("DB_PORT", "5432")
if port.lower() == "none":
    port = "5432"
db_name = os.getenv("DB_NAME", "fitness_app_db")

raw_database_url = (
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}"
)

# escape any % so ConfigParser doesn’t treat them as interpolation
escaped_url = raw_database_url.replace("%", "%%")
config.set_main_option("sqlalchemy.url", escaped_url)

from backend.application.database import Base 
target_metadata = Base.metadata

#offline migration runner 
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# online migration runner 
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

# run based on mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
