""" This module is responsible for deactivating an item
"""


from typing import Dict
from src.interactor.dtos.items.deactivate_item_dtos \
    import DeactivateItemInputDto, DeactivateItemOutputDto
from src.interactor.interfaces.presenters.items.deactivate_item_presenter \
    import DeactivateItemPresenterInterface
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.validations.items.deactivate_item_validator \
    import DeactivateItemInputDtoValidator
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException


class DeactivateItemUseCase:
    """ Deactivate Item Use Case
    """

    def __init__(
        self,
        presenter: DeactivateItemPresenterInterface,
        repository: ItemRepositoryInterface,
        logger: LoggerInterface,
    ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self, input_dto: DeactivateItemInputDto) -> Dict:
        """ This method is responsible for deactivating an item
        :param input_dto: The input data
        :type input_dto: DeactivateItemInputDto
        :return: Dict
        """
        validator = DeactivateItemInputDtoValidator(input_dto.to_dict())
        validator.validate()
        item = self.repository.deactivate(input_dto.item_id)
        if item is None:
            self.logger.log_exception("Item not found")
            raise ItemNotFoundException("id", input_dto.item_id)
        output_dto = DeactivateItemOutputDto(item)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Item Deactivated Successfully")
        return presenter_response
