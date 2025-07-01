from sqlalchemy.orm import Session
from models import UserProfile
from schemas import UserProfileCreate, UserProfileRead

#allows the user to create their profile on the application and enter details such as name, age, fitness level etc.
def create_user_profile(db: Session, user_id: int, profile: UserProfileCreate):
    user_profile = UserProfile(
        UserID = user_id,
        FullName = profile.FullName,
        Age = profile.Age,
        HeightCM = profile.Height,
        WeightKG = profile.Weight,
        FitnessLevel = profile.FitnessLevel,
        Goal = profile.Goal,
        InjuriesOrLimitations = profile.InjuriesOrLimitations 
    )
    db.add(user_profile)
    db.commit()
    db.refresh(user_profile)
    return user_profile

