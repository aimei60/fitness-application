"""
Sets up the database connection for FastAPI.
Loads environment variables, creates the SQLAlchemy engine and the session factory.
"""

import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv("sens.env")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (f"postgresql+psycopg2://"
                f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

engine = create_engine(DATABASE_URL, echo=True, pool_size=5, max_overflow=10) #Chosen 15 max connections as there won't be many users using this application at the same time.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

