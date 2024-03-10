""" Flask PostgreSQL Blueprint for get item by name
"""


from flask import jsonify
from flask import Blueprint, request, current_app
from src.app.flask_postgresql.controllers.items.get_item_by_name_controller \
    import GetItemByNameController


blueprint_get_item_by_name = Blueprint("get_item_by_name", __name__)


@blueprint_get_item_by_name.route("/item/name/", methods=["GET"])
def get_item_by_name_blueprint():
    """ Get Item By Name Blueprint
    """
    logger = current_app.config["logger"]
    controller = GetItemByNameController(logger)
    controller.get_item_info(request.args)
    result = controller.execute()
    return jsonify(result), 200
