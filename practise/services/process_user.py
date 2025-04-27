from practise.db.database_engine_factory import db
from practise.db.database_executor import DatabaseExecutor
from practise.models.users import User


def get_all_users():
    query = User.get_users()
    engine = db.get_engine()
    with engine.connect() as conn:
        data = DatabaseExecutor.fetch_results(query, conn)

    return data


def post_user(name, email):
    query = User.post_user(name, email)
    engine = db.get_engine()

    with engine.connect() as conn:
        DatabaseExecutor.insert_rows(query, conn)
