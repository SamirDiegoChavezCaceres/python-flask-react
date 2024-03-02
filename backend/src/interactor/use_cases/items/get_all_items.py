""" This module is responsible for retrieving all items
"""


from typing import Dict
from src.interactor.dtos.items.get_all_items_dtos \
    import GetAllItemsOutputDto
from src.interactor.interfaces.presenters.items.get_all_items_presenter \
    import GetAllItemsPresenterInterface
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemsNotFoundException


class GetAllItemsUseCase:
    """ This class is responsible for retrieving all items
    """

    def __init__(
        self,
        presenter: GetAllItemsPresenterInterface,
        repository: ItemRepositoryInterface,
        logger: LoggerInterface,
    ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self) -> Dict:
        """ This method is responsible for retrieving all items
        :return: Dict
        """
        items = self.repository.get_all()
        if items is None:
            self.logger.log_exception("Items not found")
            raise ItemsNotFoundException()
        output_dto = GetAllItemsOutputDto(items)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Items Retrieved Successfully")
        return presenter_response
