""" Get Item By Codebar Controller Module
"""


from typing import Dict
from src.interactor.use_cases.items.get_item_by_codebar \
    import GetItemByCodebarUseCase
from src.infra.repositories.item_postgresql_repository \
    import ItemPostgreSQLRepository
from src.interactor.dtos.items.get_by_codebar_dtos \
    import GetItemByCodebarInputDto
from src.app.flask_postgresql.interfaces.flask_postgresql_controller_interface \
    import FlaskPostgresqlControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.app.flask_postgresql.presenters.items.get_item_by_codebar_presenter \
    import GetItemByCodebarPresenter


class GetItemByCodebarController(FlaskPostgresqlControllerInterface):
    """ Get Item By Codebar Controller Class
    """
    def __init__(self, logger: LoggerInterface):
        self.logger = logger
        self.input_dto = GetItemByCodebarInputDto


    def get_item_info(self, json_input) -> None:
        """ Get item info
        :param json_input: Input data
        :raises: ValueError if item codebar is missing
        """
        if "codebar" in json_input:
            codebar = json_input["codebar"]
        else:
            raise ValueError("Missing Item Codebar")
        self.input_dto = GetItemByCodebarInputDto(
            codebar=codebar
        )


    def execute(self) -> Dict:
        """ Execute the controller
        """
        repository = ItemPostgreSQLRepository()
        presenter = GetItemByCodebarPresenter()
        use_case = GetItemByCodebarUseCase(
            repository=repository,
            presenter=presenter,
            logger=self.logger
        )
        result = use_case.execute(self.input_dto)
        return result
