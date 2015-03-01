from pytest import yield_fixture
from sqlalchemy.types import Unicode

from simple.app import app, db
from simple.mixin import BaseMixin


class SuperSimpleData(db.Model, BaseMixin):

    __tablename__ = 'simple'

    __repr_attr__ = 'id', 'created_at'


@yield_fixture
def fx_session(fx_app):
    with fx_app.app_context():
        db.create_all()
        yield db.session
        db.drop_all()


def test_base_mixin(fx_session):
    ss = SuperSimpleData()
    fx_session.add(ss)
    fx_session.commit()
    ss = SuperSimpleData.query.all()
    assert ss
    ss = ss[0]
    assert ss.id
    assert ss.created_at
    expected = 'SuperSimpleData(id={}, created_at={}) @ {}'.format(
        ss.id, ss.created_at, hex(id(ss)))
    assert expected == repr(ss)
