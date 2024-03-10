""" Flask PostgreSQL Blueprint for get all items
"""


from flask import jsonify
from flask import Blueprint, current_app
from src.app.flask_postgresql.controllers.items.get_all_items_controller \
    import GetAllItemsController


blueprint_get_all_items = Blueprint("get_all_items", __name__)


@blueprint_get_all_items.route("/items/", methods=["GET"])
def get_all_items_blueprint():
    """ Get All Items Blueprint
    """
    logger = current_app.config["logger"]
    controller = GetAllItemsController(logger)
    result = controller.execute()
    return jsonify(result), 200
