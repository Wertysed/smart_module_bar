from repositories.repository import AbstractRepository
from shema.smart_module_shema import SmartModule


class SmartModuleService:
    def __init__(self, smart_module_repository: AbstractRepository):
        self.smart_module_repository = smart_module_repository

    def read_by_options(self, options: dict):
        return self.smart_module_repository.read_by_options(options)

    def create(self, shema: SmartModule):
        return self.smart_module_repository.create(shema)
