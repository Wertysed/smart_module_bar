from repositories.repository import SqlAlchemyRepository
from models.sex import Sex 

class SexRepository(SqlAlchemyRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(session, Sex)

