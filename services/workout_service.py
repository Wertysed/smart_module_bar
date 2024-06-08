from repositories.repository import AbstractRepository
from datetime import date
from shema.athlete_shema import AthleteSh
from shema.workout_shema import CreateWorkout, PublicPullUps, Workout
from shema.smart_module_shema import SmartModule
class WorkoutService:

    def __init__(self, workout_repository: AbstractRepository, athlete_repository: AbstractRepository, smart_module_repository: AbstractRepository):
        self.workout_repository: AbstractRepository = workout_repository
        self.athlete_repository: AbstractRepository = athlete_repository
        self.smart_module_repository: AbstractRepository = smart_module_repository

    def create(self, shema: Workout):
        if not self.athlete_repository.read_by_options({"key": shema.key}):
            self.athlete_repository.create(AthleteSh(**shema.dict()))
        athlete_id = self.athlete_repository.read_by_options({"key": shema.key})[0].id
        return self.workout_repository.create(CreateWorkout(**shema.dict(), athlete_id=athlete_id,
                                                                count_of_pull_up_great=0, data=date.today()))

    def start(self, shema: Workout):
        self.create(shema)
        smart_module = self.smart_module_repository.read_by_options({"identification": shema.identification_key})[0]
        smart_module.session_status = 1
        smart_module.user_id = shema.user_id
        self.smart_module_repository.update(smart_module.id,  SmartModule.model_validate(smart_module, from_attributes=True))
        return True 

    def end(self, user_id: int, identification_key: str):
        smart_module = self.smart_module_repository.read_by_options({"identification": identification_key})[0]
        smart_module.session_status = 0
        return self.smart_module_repository.update(smart_module.id,  SmartModule.model_validate(smart_module, from_attributes=True))
    
    def update_pulls(self, shema: PublicPullUps):
        smart_module = self.smart_module_repository.read_by_options({"identification": shema.identification})[0]
        workout_last= self.workout_repository.read_by_options({"user_id": smart_module.user_id})[-1]
        if smart_module.session_status == 1:
            workout_last.count_of_pull_up_great += shema.count_of_pull_up_great
            return self.workout_repository.update(workout_last.id, CreateWorkout.model_validate(workout_last, from_attributes=True))
        else:
            return False

    def read_by_options(self, options: dict):
        return self.workout_repository.read_by_options(options)
    
    def read_by_id(self, id: int):
        return self.workout_repository.read_by_id(id)

