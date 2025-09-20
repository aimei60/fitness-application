#sets up the database connection for FastAPI, loads environment variables, creates the SQLAlchemy engine and the session factory

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Load sens.env only when running locally (not on Fly)
if not os.getenv("FLY_APP_NAME"):
    env_file = Path(__file__).resolve().parent.parent / "sens.env"
    if env_file.exists():
        load_dotenv(env_file, override=False)  # don't override real env

# Use one env var for everything
DB_URL = os.getenv("DATABASE_URL")
if not DB_URL:
    raise RuntimeError("Set DATABASE_URL (via Fly secrets in prod, sens.env locally)")

# Neon safety: ensure TLS
if "neon.tech" in DB_URL and "sslmode=" not in DB_URL:
    DB_URL += ("&" if "?" in DB_URL else "?") + "sslmode=require"

engine = create_engine(DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()