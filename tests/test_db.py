from sqlalchemy import select

from models.models import User


def test_create_user(session):
    user = User(
        username='Dayvd',
        email='ally@gmail.com',
        password='dayvd123',
    )

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'ally@gmail.com'))

    assert result.username == 'Dayvd'
