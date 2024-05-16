from abc import ABC, abstractmethod
from fastapi import Depends
from db import get_db
from sqlalchemy.orm import selectinload

class AbstractRepository(ABC):
    @abstractmethod
    def read_by_options(self, options: dict):
        raise NotImplementedError

    @abstractmethod
    def read_by_id(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def create(self, shema):
        raise NotImplementedError

    @abstractmethod
    def update(self, id: int, shema):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session, model):
        self.session = session
        self.model = model

    def read_by_options(self, options: dict):
        query = self.session.query(self.model)
        query = query.options(selectinload('*'))
        for attr, value in options.items():
            query = query.filter(getattr(self.model, attr) == value)

        return query.all()

    def read_by_id(self, id: int):
        query = self.session.query(self.model)

        query = query.filter(self.model.id == id).first()
        if not query:
            return 0
        return query

    def create(self, shema):
        query = self.model(**shema.dict())

        self.session.add(query)
        self.session.commit()
        self.session.refresh(query)

        return query

    def update(self, id: int, shema):
        self.session.query(self.model).filter(self.model.id == id).update(shema.dict(exclude_none=True))
        self.session.commit()
        return self.read_by_id(id)
