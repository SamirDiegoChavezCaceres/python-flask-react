""" Create Item Controller Module
"""


from typing import Dict
from src.interactor.use_cases.items.create_item import CreateItemUseCase
from src.infra.repositories.item_postgresql_repository \
    import ItemPostgreSQLRepository
from src.interactor.dtos.items.create_item_dtos import CreateItemInputDto
from src.app.flask_postgresql.interfaces.flask_postgresql_controller_interface \
    import FlaskPostgresqlControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.app.flask_postgresql.presenters.items.create_item_presenter \
    import CreateItemPresenter


class CreateItemController(FlaskPostgresqlControllerInterface):
    """ Create Item Controller Class
    """
    def __init__(self, logger: LoggerInterface):
        self.logger = logger
        self.input_dto = CreateItemInputDto


    def get_item_info(self, json_input) -> None:
        """ Get item info
        :param json_input: Input data
        :raises: ValueError if item name or others are missing
        """
        if "codebar" in json_input:
            codebar = json_input["codebar"]
        else:
            raise ValueError("Missing Item Codebar")
        if "name" in json_input:
            name = json_input["name"]
        else:
            raise ValueError("Missing Item Name")
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
        self.input_dto = CreateItemInputDto(
            codebar=codebar,
            name=name,
            description=description,
            price=price,
            stock=stock
        )


    def execute(self) -> Dict:
        """ Execute the controller
        :returns: Item Created
        """
        repository = ItemPostgreSQLRepository()
        presenter = CreateItemPresenter()
        use_case = CreateItemUseCase(repository, presenter, self.logger)
        result = use_case.execute(self.input_dto)
        return result
