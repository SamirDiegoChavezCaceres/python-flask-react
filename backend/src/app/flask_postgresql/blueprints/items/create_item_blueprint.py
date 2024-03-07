""" Flask PostgreSQL Blueprint for create item
"""


from flask import jsonify
from flask import Blueprint, request, current_app
from src.app.flask_postgresql.controllers.items.create_item_controller \
    import CreateItemController


blueprint_create_item = Blueprint("create_item", __name__)


@blueprint_create_item.route("/item/", methods=["POST"])
def create_item_blueprint():
    """ Create Item Blueprint
    """
    logger = current_app.config["logger"]
    input_json = request.get_json(force=True)
    controller = CreateItemController(logger)
    controller.get_item_info(input_json)
    result = controller.execute()
    return jsonify(result), 201
