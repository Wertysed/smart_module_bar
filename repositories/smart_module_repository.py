from repositories.repository import SqlAlchemyRepository
from models.smart_module import SmartModule 

class SmartModuleRepository(SqlAlchemyRepository):
    def __init__(self, session):
        self.session = session
        super().__init__(session, SmartModule)


