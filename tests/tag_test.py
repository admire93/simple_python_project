from simple.tag import Tag

def test_create_tag(fx_session, fx_user):
    tag_name = 'sleeping'
    tag = Tag(name=tag_name, user=fx_user)
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
    assert queried.user_id == fx_user.id


def test_backref_tags(fx_session, fx_user):
    for x in range(1, 10):
        tag_name = 'sleeping{}'
        tag = Tag(name=tag_name, user=fx_user)
        fx_session.add(tag)
        queried = Tag.query \
                  .filter_by(name=tag_name) \
                  .all()
    fx_session.commit()
    assert len(fx_user.tags) == 9
    for q_tag in fx_user.tags:
        assert q_tag.name.startswith('sleeping')
