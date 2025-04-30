from sqlalchemy_test.app.test_database import Base, engine
from database import workouts, workout_sections, workoutRoutine, User, UserWorkoutRequest, UserProfile

print("Creating all tables in test_db...")
Base.metadata.create_all(engine)
print("Done.")