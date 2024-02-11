""" Base class for all models
"""


from configs import config
import pymongo


class Base():
    """ Base class for all models
    """


client = pymongo.MongoClient(config.DB_URI)
Session = client[config.DB_NAME]
