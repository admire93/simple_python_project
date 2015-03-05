from datetime import datetime

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, DateTime
from sqlalchemy.orm import relationship

from .db import db
from .mixin import BaseMixin

class Tag(db.Model, BaseMixin):

    __tablename__ = 'tags'

    __repr_attr__ = 'name',

    name = Column(Unicode, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', backref='tags')
