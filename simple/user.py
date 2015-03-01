from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode, DateTime

from .app import db
from .mixin import BaseMixin

class User(db.Model, BaseMixin):

    __tablename__ = 'users'

    name = Column(Unicode, nullable=False)
