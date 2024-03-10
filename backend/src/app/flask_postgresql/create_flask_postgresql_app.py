""" Main Flask PostgreSQL App
"""


from flask import Flask, g
from werkzeug.exceptions import HTTPException
from src.app.flask_postgresql.blueprints.items.create_item_blueprint\
    import blueprint_create_item
from src.app.flask_postgresql.blueprints.items.delete_item_blueprint\
    import blueprint_delete_item
from src.app.flask_postgresql.blueprints.items.update_item_blueprint\
    import blueprint_update_item
from src.app.flask_postgresql.blueprints.items.get_item_blueprint\
    import blueprint_get_item
from src.app.flask_postgresql.blueprints.items.get_item_by_codebar_blueprint\
    import blueprint_get_item_by_codebar
from src.app.flask_postgresql.blueprints.items.get_item_by_name_blueprint\
    import blueprint_get_item_by_name
from src.app.flask_postgresql.blueprints.items.activate_item_blueprint\
    import blueprint_activate_item
from src.app.flask_postgresql.blueprints.items.deactivate_item_blueprint\
    import blueprint_deactivate_item
from src.app.flask_postgresql.blueprints.items.get_all_items_blueprint\
    import blueprint_get_all_items

from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import FieldValueNotPermittedException
from src.infra.db_models.postgresql.postgresql_base import session
from src.interactor.errors.error_classes import UniqueViolationError
from src.app.flask_postgresql.blueprints.home_blueprint import blueprint_home

def format_error_response(
        error: Exception,
        error_code: int,
        logger: LoggerInterface
):
    """ Format error response """
    logger.log_exception(f"500 - Internal Server Error: {str(error)}")

    response = {
        'status_code': error_code,
        'error': error.__class__.__name__,
        'message': str(error)
    }
    return response, error_code


def create_flask_postgresql_app(logger: LoggerInterface):
    """ Create Flask PostgreSQL App """
    app = Flask(__name__)
    app.config['logger'] = logger
    app.register_blueprint(blueprint_home, url_prefix='/')

    app.register_blueprint(blueprint_create_item, url_prefix='/v1')
    app.register_blueprint(blueprint_delete_item, url_prefix='/v1')
    app.register_blueprint(blueprint_update_item, url_prefix='/v1')
    app.register_blueprint(blueprint_get_item, url_prefix='/v1')

    app.register_blueprint(blueprint_get_item_by_codebar, url_prefix='/v1')
    app.register_blueprint(blueprint_get_item_by_name, url_prefix='/v1')
    app.register_blueprint(blueprint_activate_item, url_prefix='/v1')
    app.register_blueprint(blueprint_deactivate_item, url_prefix='/v1')
    app.register_blueprint(blueprint_get_all_items, url_prefix='/v1')


    @app.errorhandler(HTTPException)
    def handle_http_exception(error: HTTPException):
        """ Handle HTTP Exception """
        logger.log_exception(str(error.__class__.__name__))
        logger.log_exception(str(error.description))
        response = {
            'error': error.__class__.__name__,
            'message': error.description,
        }
        return response, error.code

    @app.errorhandler(ValueError)
    def handle_value_error(error: ValueError):
        """ Handle Value Error Response """
        return format_error_response(error, 400, logger)

    @app.errorhandler(FieldValueNotPermittedException)
    def handle_field_not_permitted_error(
        error: FieldValueNotPermittedException
    ):
        """ Handle Value Error Response """
        return format_error_response(error, 400, logger)

    @app.errorhandler(UniqueViolationError)
    def handle_unique_violation_error(error: UniqueViolationError):
        """ Handle Unique Violation Error Response """
        return format_error_response(error, 409, logger)

    @app.errorhandler(Exception)
    def handle_general_exception(error):
        """ Handle Other Errors Response """
        return format_error_response(error, 500, logger)

    @app.before_request
    def before_request():
        """ Before Request """
        g.db = session()

    @app.teardown_request
    def teardown_request(_unused=False):
        """ After Request """
        dbc = getattr(g, 'db', None)
        if dbc is not None:
            dbc.close()

    return app
