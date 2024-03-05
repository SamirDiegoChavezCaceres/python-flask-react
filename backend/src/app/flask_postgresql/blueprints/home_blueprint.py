""" Flask MongoDB Home Blueprint
"""


from flask import Blueprint, jsonify, request, current_app


blueprint_home = Blueprint('home', __name__)


@blueprint_home.route('/', methods=['GET'])
def home_blueprint():
    """ Home Blueprint
    """
    current_app.config['logger'].log_info("Home Blueprint")
    return jsonify({"message": "Welcome to Flask PostgreSQL"}), 200
