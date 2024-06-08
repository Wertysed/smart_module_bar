from repositories.repository import SqlAlchemyRepository
from models.athlete import Athlete 

class AthleteRepository(SqlAlchemyRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(session, Athlete)

