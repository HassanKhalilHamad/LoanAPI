from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from pathlib import Path

def startup():
    engine = create_engine("sqlite:///jobstores.db")
    if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))

startup()