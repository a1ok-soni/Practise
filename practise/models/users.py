from sqlalchemy import Column, Integer, String, insert, select
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    @classmethod
    def get_users(cls):
        """
        Fetches list of all users
        """
        query = select(cls)
        return query

    @classmethod
    def post_user(cls, name, email):
        """
        Inserts a user to db
        """

        query = insert(cls).values(name=name, email=email)
        return query
