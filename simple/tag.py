from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode, DateTime

from .app import db
from .mixin import BaseMixin

class Tag(db.Model, BaseMixin):

    __tablename__ = 'tags'

    name = Column(Unicode, nullable=False)
