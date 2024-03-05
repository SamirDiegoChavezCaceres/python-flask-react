""" Flask MongoDB Create Item Blueprint
"""


from flask import Blueprint, jsonify, request, current_app
from src.app.flask_mongodb.controllers.items.create_item_controller import \
    CreateItemController


blueprint_home = Blueprint('create_item', __name__)


@blueprint_home.route('/create_item', methods=['POST'])
def create_item_blueprint():
    """ Create Item Blueprint
    """
    logger = current_app.config['logger']
    input_json = request.get_json(force=True)
    controller = CreateItemController(logger)
    controller.get_item_info(input_json)
    result = controller.execute()
    return jsonify(result), 201
