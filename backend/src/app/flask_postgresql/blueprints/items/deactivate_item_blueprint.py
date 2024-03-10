""" Flask PostgreSQL Blueprint for deactivate item
"""


from flask import jsonify
from flask import Blueprint, request, current_app
from src.app.flask_postgresql.controllers.items.deactivate_item_controller \
    import DeactivateItemController


blueprint_deactivate_item = Blueprint("deactivate_item", __name__)


@blueprint_deactivate_item.route("/item/deactivate/", methods=["PUT"])
def deactivate_item_blueprint():
    """ Deactivate Item Blueprint
    """
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = DeactivateItemController(logger)
    controller.get_item_info(input_json)
    result = controller.execute()
    return jsonify(result), 200
