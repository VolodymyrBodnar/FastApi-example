from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class UserCreate(BaseModel):
    username: str
    password: str
