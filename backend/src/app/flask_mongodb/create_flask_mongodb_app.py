""" Main Flask MongoDB app
"""


from flask import Flask, g
from flask_cors import CORS
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.infra.db_models.mongodb.mongodb_base import session, client
#from src.app.flask_mongodb.blueprints.home_blueprint import blueprint_home


def format_error_response(
        error: Exception,
        error_code: int,
        logger: LoggerInterface
):
    """ Format Error Response
    """
    logger.log_exception(f"500 - Internal Server Error: {str(error)}")

    response = {
        'status_code': error_code,
        'error': error.__class__.__name__,
        'message': str(error)
    }
    return response, error_code


def create_flask_mongodb_app(logger: LoggerInterface):
    """ Create Main Flask MongoDB app
    """
    app = Flask(__name__)
    app.config['logger'] = logger
    #app.register_blueprint(blueprint_home, url_prefix='/')

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
