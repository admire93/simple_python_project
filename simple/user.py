from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode, DateTime

from .db import db
from .mixin import BaseMixin

class User(db.Model, BaseMixin):

    __tablename__ = 'users'

    __repr_attr__ = 'name',

    name = Column(Unicode, nullable=False)
