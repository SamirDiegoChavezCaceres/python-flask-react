""" Get Item By Name Controller Module
"""


from typing import Dict
from src.interactor.use_cases.items.get_item_by_name \
    import GetItemByNameUseCase
from src.infra.repositories.item_postgresql_repository \
    import ItemPostgreSQLRepository
from src.interactor.dtos.items.get_item_by_name_dtos \
    import GetItemByNameInputDto
from src.app.flask_postgresql.interfaces.flask_postgresql_controller_interface \
    import FlaskPostgresqlControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.app.flask_postgresql.presenters.items.get_item_by_name_presenter \
    import GetItemByNamePresenter


class GetItemByNameController(FlaskPostgresqlControllerInterface):
    """ Get Item By Name Controller Class
    """
    def __init__(self, logger: LoggerInterface):
        self.logger = logger
        self.input_dto = GetItemByNameInputDto


    def get_item_info(self, json_input) -> None:
        """ Get item info
        :param json_input: Input data
        :raises: ValueError if item name is missing
        """
        if "name" in json_input:
            name = json_input["name"]
        else:
            raise ValueError("Missing Item Name")
        self.input_dto = GetItemByNameInputDto(
            name=name
        )


    def execute(self) -> Dict:
        """ Execute the controller
        """
        repository = ItemPostgreSQLRepository()
        presenter = GetItemByNamePresenter()
        use_case = GetItemByNameUseCase(
            repository=repository,
            presenter=presenter,
            logger=self.logger
        )
        result = use_case.execute(self.input_dto)
        return result
