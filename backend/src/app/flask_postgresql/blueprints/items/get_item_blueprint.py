""" Flask PostgreSQL Blueprint for get item
"""


from flask import jsonify
from flask import Blueprint, request, current_app
from src.app.flask_postgresql.controllers.items.get_item_controller \
    import GetItemController


blueprint_get_item = Blueprint("get_item", __name__)


@blueprint_get_item.route("/item/", methods=["GET"])
def get_item_blueprint():
    """ Get Item Blueprint
    """
    logger = current_app.config["logger"]
    controller = GetItemController(logger)
    controller.get_item_info(request.args)
    result = controller.execute()
    return jsonify(result), 200
