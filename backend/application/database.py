"""
Sets up the database connection for FastAPI.
Loads environment variables, creates the SQLAlchemy engine and the session factory. Includes environment variable loading for database credentials.
"""

import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

load_dotenv("sens.env")

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_NAME = os.environ.get("DB_NAME")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")

DATABASE_URL = (f"postgresql+psycopg2://"
                f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

print("Using Database:", DATABASE_URL)

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
#Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

