from sqlalchemy import Engine, create_engine

from practise.environment import Environment as Env


class DataBaseEngineFactory:
    _instance = None
    pg_engine: Engine = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()

        return cls._instance

    def __init__(self):
        if DataBaseEngineFactory._instance:
            raise Exception("Only single instance allowed!")

    def initialize(self):
        self.pg_engine: Engine = self.get_engine()
        self.pg_engine.dispose()

    def get_engine(self):
        return create_engine(
            f"postgresql://{Env.PG_Username}:{Env.PG_Password}@{Env.PG_Host}/"
        )


db = DataBaseEngineFactory.get_instance()
