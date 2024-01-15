from fastapi import FastAPI, HTTPException, Depends, status
from api.todo_items import router as todo_router
from models import todo
from depenedencies.database import engine
import json
import jwt
import datetime


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

todo.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo_router, prefix="/todo")

secret_key = "secret_key"


@app.get("/")
async def health_check():
    print()
    return {"OK": True}


# Маркери для авторизації та отримання даних користувача
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



@app.post("/register/", response_model=User)
async def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Користувач з таким іменем вже існує")
    
    return User(**user.dict())


@app.post("/token/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if user is None or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неправильний логін або пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token({"username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/protected-resource/", response_model=User)
async def protected_resource(current_user: User = Depends(get_current_user)):
    return current_user


