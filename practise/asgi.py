from practise.app import create_app
from practise.db.database_engine_factory import db

app = create_app()
db.initialize()
