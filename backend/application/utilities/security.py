from passlib.context import CryptContext

#creates a passsword hasing manager (pwd_context) using the bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#adds hashed password into the db
def get_password_hash(password):
    return pwd_context.hash(password)  

#checks if the user password matches the hashed password stored in db
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


