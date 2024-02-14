""" Main Flask MongoDB app
"""


from flask import Flask, g
from flask_cors import CORS
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.infra.db_models.db_base import session, client


def create_flask_mongodb_app(logger: LoggerInterface):
    """ Create Main Flask MongoDB app
    """
    app = Flask(__name__)
    app.config['logger'] = logger

    @app.before_request
    def before_request():
        """ Before Request """
        g.cli = client
        g.db = session

    @app.teardown_request
    def teardown_request(_unused=False):
        """ After Request """
        dbc = getattr(g, 'cli', None)
        if dbc is not None:
            dbc.close()

    return app
