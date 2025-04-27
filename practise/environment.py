from os import environ

from dotenv import load_dotenv

load_dotenv()


class Environment:
    PG_Username = environ["PG_USERNAME"]
    PG_Password = environ["PG_PASSWORD"]
    PG_Host = environ["PG_HOST"]
