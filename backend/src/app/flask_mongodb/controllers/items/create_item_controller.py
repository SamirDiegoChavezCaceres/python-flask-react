# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-module-docstring


from typing import Dict
from src.app.flask_mongodb.interfaces.flask_mongodb_controller_interface\
    import FlaskMongoDBControllerInterface


class CreateItemController(FlaskMongoDBControllerInterface):
    def get_item_info(self, json_input) -> None:
        pass

    def execute(self) -> Dict:
        pass
