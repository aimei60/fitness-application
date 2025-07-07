"""
Drops all tables or clears necessary data from the test_db database e.g. mistakes or incorrect data entered.
Intended for use in testing environments only.
"""

from sqlalchemy_test.app.test_database import Base, engine, SessionLocal
from application.database import workouts



    