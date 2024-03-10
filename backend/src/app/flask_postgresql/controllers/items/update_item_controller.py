""" Update Item Controller Module
"""


from typing import Dict
from src.interactor.use_cases.items.update_item import UpdateItemUseCase
from src.infra.repositories.item_postgresql_repository \
    import ItemPostgreSQLRepository
from src.interactor.dtos.items.update_item_dtos import UpdateItemInputDto
from src.app.flask_postgresql.interfaces.flask_postgresql_controller_interface \
    import FlaskPostgresqlControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.app.flask_postgresql.presenters.items.update_item_presenter \
    import UpdateItemPresenter


class UpdateItemController(FlaskPostgresqlControllerInterface):
    """ Update Item Controller Class
    """
    def __init__(self, logger: LoggerInterface):
        self.logger = logger
        self.input_dto = UpdateItemInputDto

    def get_item_info(self, json_input) -> None:
        """ Get item info
        :param json_input: Input data
        :raises: ValueError if item_id, name, codebar, description, price or stock are missing
        """
        if "item_id" in json_input:
            item_id = json_input["item_id"]
        else:
            raise ValueError("Missing Item ID")
        if "name" in json_input:
            name = json_input["name"]
        else:
            raise ValueError("Missing Item Name")
        if "codebar" in json_input:
            codebar = json_input["codebar"]
        else:
            raise ValueError("Missing Item Codebar")
        if "description" in json_input:
            description = json_input["description"]
        else:
            raise ValueError("Missing Item Description")
        if "price" in json_input:
            price = json_input["price"]
        else:
            raise ValueError("Missing Item Price")
        if "stock" in json_input:
            stock = json_input["stock"]
        else:
            raise ValueError("Missing Item Stock")
        if "state" in json_input:
            state = json_input["state"]
        else:
            raise ValueError("Missing Item State")
        self.input_dto = UpdateItemInputDto(
            item_id=item_id,
            name=name,
            codebar=codebar,
            description=description,
            price=price,
            stock=stock,
            state=state
        )

    def execute(self) -> Dict:
        """ Execute the controller
        """
        repository = ItemPostgreSQLRepository()
        presenter = UpdateItemPresenter()
        use_case = UpdateItemUseCase(
            repository=repository,
            presenter=presenter,
            logger=self.logger
        )
        result = use_case.execute(self.input_dto)
        return result
