#creates the test_db database and initializes the schema.

from sqlalchemy_test.app.test_database import Base, engine
from backend.application.database import workouts, workout_sections, workoutRoutine, User, UserWorkoutRequest, UserProfile

print("Creating all tables in test_db...")
#Base.metadata.create_all(engine)
print("Done.")