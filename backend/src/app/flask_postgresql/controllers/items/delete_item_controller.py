""" Delete Item Controller Module
"""


from typing import Dict
from src.interactor.use_cases.items.delete_item import DeleteItemUseCase
from src.infra.repositories.item_postgresql_repository \
    import ItemPostgreSQLRepository
from src.interactor.dtos.items.delete_item_dtos import DeleteItemInputDto
from src.app.flask_postgresql.interfaces.flask_postgresql_controller_interface \
    import FlaskPostgresqlControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.app.flask_postgresql.presenters.items.delete_item_presenter \
    import DeleteItemPresenter


class DeleteItemController(FlaskPostgresqlControllerInterface):
    """ Delete Item Controller Class
    """
    def __init__(self, logger: LoggerInterface):
        self.logger = logger
        self.input_dto = DeleteItemInputDto


    def get_item_info(self, json_input) -> None:
        """ Get item info
        :param json_input: Input data
        :raises: ValueError if item_id is missing
        """
        if "item_id" in json_input:
            item_id = json_input["item_id"]
        else:
            raise ValueError("Missing Item ID")
        self.input_dto = DeleteItemInputDto(
            item_id=item_id
        )


    def execute(self) -> Dict:
        """ Execute the controller
        """
        repository = ItemPostgreSQLRepository()
        presenter = DeleteItemPresenter()
        use_case = DeleteItemUseCase(
            repository=repository,
            presenter=presenter,
            logger=self.logger
        )
        return use_case.execute(self.input_dto)
