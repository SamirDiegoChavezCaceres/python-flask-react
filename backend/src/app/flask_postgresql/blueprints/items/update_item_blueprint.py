""" Flask PostgreSQL Blueprint for update item
"""


from flask import jsonify
from flask import Blueprint, request, current_app
from src.app.flask_postgresql.controllers.items.update_item_controller \
    import UpdateItemController


blueprint_update_item = Blueprint("update_item", __name__)


@blueprint_update_item.route("/item/", methods=["PUT"])
def update_item_blueprint():
    """ Update Item Blueprint
    """
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = UpdateItemController(logger)
    controller.get_item_info(input_json)
    result = controller.execute()
    return jsonify(result), 200
