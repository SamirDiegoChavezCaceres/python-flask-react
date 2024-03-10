""" Flask PostgreSQL Blueprint for delete item
"""


from flask import jsonify
from flask import Blueprint, request, current_app
from src.app.flask_postgresql.controllers.items.delete_item_controller \
    import DeleteItemController


blueprint_delete_item = Blueprint("delete_item", __name__)


@blueprint_delete_item.route("/item/", methods=["DELETE"])
def delete_item_blueprint():
    """ Delete Item Blueprint
    """
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = DeleteItemController(logger)
    controller.get_item_info(input_json)
    result = controller.execute()
    return jsonify(result), 200
