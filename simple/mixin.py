from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime

class BaseMixin(object):

    id =  Column(Integer, primary_key=True)

    created_at = Column(DateTime, default=datetime.now, nullable=False)

    __repr_attr__ = ()

    def __repr__(self):
        return '{}'.format(self.__repr_attr__)
