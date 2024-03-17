from pydantic import BaseModel

class Token(BaseModel):
    """Structure of Token"""
    access_token: str
    token_type:str

class TokenData(BaseModel):
    """Structure of data in token"""
    username: str | None = None


