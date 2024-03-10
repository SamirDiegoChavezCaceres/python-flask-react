""" Flask PostgreSQL Blueprint for activate item
"""


from flask import jsonify
from flask import Blueprint, request, current_app
from src.app.flask_postgresql.controllers.items.activate_item_controller \
    import ActivateItemController


blueprint_activate_item = Blueprint("activate_item", __name__)


@blueprint_activate_item.route("/item/activate/", methods=["PUT"])
def activate_item_blueprint():
    """ Activate Item Blueprint
    """
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = ActivateItemController(logger)
    controller.get_item_info(input_json)
    result = controller.execute()
    return jsonify(result), 200
