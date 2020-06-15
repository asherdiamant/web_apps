from data import db_session
from data.users import User


def get_user_count() -> int:
    session = db_session.create_session()

    return session.query(User).count()
