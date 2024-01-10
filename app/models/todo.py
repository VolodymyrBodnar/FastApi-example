from sqlalchemy import Column, String, Boolean

from .base import BaseModel, Base

class TodoDB(BaseModel):
    __tablename__ = "todos"
    name = Column(String)
    is_done = Column(Boolean, default=False)
    description = Column(String)

