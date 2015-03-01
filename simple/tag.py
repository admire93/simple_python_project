from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, Unicode, DateTime

from .app import db

class Tag(db.Model):

    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)

    name = Column(Unicode, nullable=False)

    created_at = Column(DateTime, default=datetime.now, nullable=False)
