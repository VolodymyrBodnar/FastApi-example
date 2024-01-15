

class Token(BaseModel):
    access_token: str | bytes
    token_type: str = "bearer"


def create_access_token(data: dict):
    token_data = {
        "sub": str(data["username"]),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)
    }
    token = jwt.encode(token_data, secret_key, algorithm="HS256")

    return token


def decode_jwt_token(token):
    try:
        # Декодуємо токен за допомогою секретного ключа
        decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return "Токен вже закінчив свій строк дії"
    except jwt.InvalidTokenError:
        return "Недійсний токен"


def verify_password(plain_password, hashed_password):
    return plain_password == hashed_password



async def get_current_user(token: str = Depends(oauth2_scheme)):
    token = decode_jwt_token(token)
    user = get_user(token.get("sub"))
    if user is None:
        raise HTTPException(status_code=401, detail="Недійсний токен")
    return user

