from abc import ABC, abstractmethod

from sqlalchemy.orm import Session


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class CreateObjectCommand(Command):
    def __init__(self, db: Session, factory, **kwargs):
        self.db = db
        self.factory = factory
        self.kwargs = kwargs

    def execute(self):
        obj = self.factory.create(**self.kwargs)
        self.db.add(obj)
        self.db.commit()
        return obj
