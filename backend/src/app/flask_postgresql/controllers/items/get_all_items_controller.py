""" Get all items Controller Module
"""


from typing import Dict
from src.interactor.use_cases.items.get_all_items import GetAllItemsUseCase
from src.infra.repositories.item_postgresql_repository \
    import ItemPostgreSQLRepository
from src.app.flask_postgresql.interfaces.flask_postgresql_controller_interface \
    import FlaskPostgresqlControllerInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.app.flask_postgresql.presenters.items.get_all_items_presenter \
    import GetAllItemsPresenter


class GetAllItemsController(FlaskPostgresqlControllerInterface):
    """ Get all items Controller Class
    """
    def __init__(self, logger: LoggerInterface):
        self.logger = logger


    def execute(self) -> Dict:
        """ Execute the controller
        """
        repository = ItemPostgreSQLRepository()
        presenter = GetAllItemsPresenter()
        use_case = GetAllItemsUseCase(
            presenter,
            repository,
            self.logger
        )
        return use_case.execute()
