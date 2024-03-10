""" Flask PostgreSQL Blueprint for get item by codebar
"""


from flask import jsonify
from flask import Blueprint, request, current_app
from src.app.flask_postgresql.controllers.items.get_item_by_codebar_controller \
    import GetItemByCodebarController


blueprint_get_item_by_codebar = Blueprint("get_item_by_codebar", __name__)


@blueprint_get_item_by_codebar.route("/item/codebar/", methods=["GET"])
def get_item_by_codebar_blueprint():
    """ Get Item By Codebar Blueprint
    """
    logger = current_app.config["logger"]
    controller = GetItemByCodebarController(logger)
    controller.get_item_info(request.args)
    result = controller.execute()
    return jsonify(result), 200
