""" Base class for all models on PostgreSQL
"""


from configs import config
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session


class Base(DeclarativeBase):
    """ Base class for all models
    """


engine = create_engine(config.DB_URI+config.DB_NAME)
session = scoped_session(sessionmaker(bind=engine))
