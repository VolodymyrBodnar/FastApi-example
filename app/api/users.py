from fastapi import APIRouter, Depends
from depenedencies.database import get_db, SessionLocal
from depenedencies.auth import create_access_token, DefaultUser
from schemas.user import User
from services.users import UserService
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


@router.post("/register/", response_model=User)
async def register(user: User, db: SessionLocal = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_new(user)


@router.get("/protected-resource/", response_model=User)
async def protected_resource(current_user: DefaultUser):
    return current_user
