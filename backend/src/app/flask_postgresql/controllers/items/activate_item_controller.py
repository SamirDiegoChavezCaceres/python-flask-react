""" Activate Item Controller Module
"""


from typing import Dict
from src.interactor.use_cases.items.activate_item import ActivateItemUseCase
from src.infra.repositories.item_postgresql_repository \
    import ItemPostgreSQLRepository
from src.interactor.dtos.items.activate_item_dtos \
    import ActivateItemInputDto
from src.app.flask_postgresql.interfaces.flask_postgresql_controller_interface \
    import FlaskPostgresqlControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.app.flask_postgresql.presenters.items.activate_item_presenter \
    import ActivateItemPresenter


class ActivateItemController(FlaskPostgresqlControllerInterface):
    """ Activate Item Controller Class
    """
    def __init__(self, logger: LoggerInterface):
        self.logger = logger
        self.input_dto = ActivateItemInputDto


    def get_item_info(self, json_input) -> None:
        """ Get item info
        :param json_input: Input data
        :raises: ValueError if item_id is missing
        """
        if "item_id" in json_input:
            item_id = json_input["item_id"]
        else:
            raise ValueError("Missing Item ID")
        self.input_dto = ActivateItemInputDto(
            item_id=item_id
        )


    def execute(self) -> Dict:
        """ Execute the controller
        """
        repository = ItemPostgreSQLRepository()
        presenter = ActivateItemPresenter()
        use_case = ActivateItemUseCase(
            repository=repository,
            presenter=presenter,
            logger=self.logger
        )
        return use_case.execute(self.input_dto)
