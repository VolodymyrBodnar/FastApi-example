from sqlalchemy import Column, String, Boolean

from .base import BaseModel, Base

class UserDB(BaseModel):
    __tablename__ = "users"
    username = Column(String)
    password = Column(String)
    salt = Column(String)
    role = Column(String)

