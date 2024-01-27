from fastapi import APIRouter, Depends, Request, HTTPException, File, UploadFile
from depenedencies.database import get_db, SessionLocal
from depenedencies.auth import DefaultUser
from schemas.user import User, UserActivation
from services.users import UserService

from depenedencies.rate_limiter import RateLimiter
from depenedencies.cloudinary_client import get_uploader

router = APIRouter()

rate_limiter = RateLimiter(3, 120)

async def rate_limit(request: Request):
    global rate_limiter
    client_id = request.client.host
    if not rate_limiter.is_allowed(client_id):
        raise HTTPException(status_code=429, detail="Too Many Requests")
    return True


@router.post("/register/", response_model=User)
async def register(user: User, db: SessionLocal = Depends(get_db), rl=Depends(rate_limit)):
    user_service = UserService(db)
    return user_service.create_new(user)


@router.get("/protected-resource/", response_model=User)
async def protected_resource(current_user: DefaultUser, rl=Depends(rate_limit)):
    return current_user


@router.post("/activate/", response_model=User)
async def activate(data: UserActivation, db: SessionLocal = Depends(get_db)):
    user_service = UserService(db)
    return user_service.activate_user(data)





@router.post("/upload_image")
def upload(current_user: DefaultUser, file: UploadFile = File(...), uploader = Depends(get_uploader), db: SessionLocal = Depends(get_db)):
    try:
        current_user
        user_service = UserService(db)
        contents = file.file.read()
        responce = uploader.upload(contents, public_id=file.filename)
        responce.get('secure_url')
        user_service.set_image(current_user, responce.get('secure_url'))

    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}

