from simple.tag import Tag

def test_create_tag(fx_session):
    tag_name = 'sleeping'
    tag = Tag(name=tag_name)
    fx_session.add(tag)
    fx_session.commit()
    queried = Tag.query \
              .filter_by(name=tag_name) \
              .all()
    assert 1 == len(queried)
    queried = queried[0]
    assert queried
    assert queried.id
    assert queried.created_at
    assert queried.name
    assert tag_name == tag.name
