from repo.user import UserRepo
from schemas.user import User
from models.users import UserDB

from fastapi import HTTPException

class UserService():
    def __init__(self, db) -> None:
        self.repo = UserRepo(db=db)

    def create_new(self, user: User) -> User:
        new_user_from_db = self.repo.create(user)
        new_user = User.from_orm(new_user_from_db)
        return new_user


    def get_user_for_auth(self, username: str, password: str) -> User:
        user = self.repo.get_user_and_check_pass(username, password)
        if user is None:
            raise HTTPException(status_code=403)
        return User.from_orm(user)

    def get_by_username(self, username: str)  -> User:
        user = self.repo.get_by_username(username)
        if user is None:
            raise HTTPException(status_code=403)
        return User.from_orm(user)


