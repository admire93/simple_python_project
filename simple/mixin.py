from datetime import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime

class BaseMixin(object):

    id =  Column(Integer, primary_key=True)

    created_at = Column(DateTime, default=datetime.now, nullable=False)

    __repr_attr__ = 'id',

    def __repr__(self):
        print()
        represents = []
        for attr in self.__repr_attr__:
            represents.append('{}={}'.format(attr, getattr(self, attr)))
        return '{0.__class__.__name__}({1})'.format(self,
                                                    ', '.join(represents))
