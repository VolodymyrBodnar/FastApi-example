from pydantic import BaseModel
import enum

class RolesEnum(str, enum.Enum):
    USER = "user"
    MANAGER = "manager"
    ADMIN = "ADMIN"

class User(BaseModel):
    username: str
    password: str
    role: RolesEnum

    class Config:
        orm_mode = True
        from_attributes=True
