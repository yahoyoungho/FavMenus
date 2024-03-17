from pydantic import BaseModel

class User(BaseModel):
    """Structure of user model"""
    username:str # equiv. to email
    first_name: str | None = None
    last_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    """Child structure of user with hashed password"""
    hashed_password: str