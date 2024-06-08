from repositories.repository import SqlAlchemyRepository
from models.workout import Workout 

class WorkoutRepository(SqlAlchemyRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(session, Workout)
