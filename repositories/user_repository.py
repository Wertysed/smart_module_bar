from repositories.repository import SqlAlchemyRepository
from models import User


class UserRepository(SqlAlchemyRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(session, User)


         
