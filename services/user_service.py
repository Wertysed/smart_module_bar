from repositories.repository import AbstractRepository
from shema.users_shema import UserIn, UserReg, UserCreate
from utils import get_password_hash, verify_password

class UserService:
    def __init__(self, user_repository: AbstractRepository):
        self.user_repository: AbstractRepository = user_repository 

    def sign_up(self, user_info: UserReg):
        return self.user_repository.create(UserCreate(**user_info.model_dump(), hashed_password=get_password_hash(user_info.password)))

    def sign_in(self, user_info: UserIn):
        user_db = self.user_repository.read_by_options({"email": user_info.email})[0] 
        if user_db:
            if verify_password(user_info.password, user_db.hashed_password):
                return user_db
        return False
    
    def read_by_id(self, id: int):
        return self.user_repository.read_by_id(id)
