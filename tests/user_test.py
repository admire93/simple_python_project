from simple.user import User

def test_create_user(fx_session):
    name = 'kangh'
    user = User(name=name)
    fx_session.add(user)
    fx_session.commit()
    queried = User.query \
              .filter_by(name=name) \
              .all()
    assert 1 == len(queried)
    queried = queried[0]
    assert queried
    assert queried.id
    assert queried.created_at
    assert queried.name
    assert name == queried.name
