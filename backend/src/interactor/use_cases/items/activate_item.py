""" Activate Item Use Case
"""


from typing import Dict
from src.interactor.dtos.items.activate_item_dtos \
    import ActivateItemInputDto, ActivateItemOutputDto
from src.interactor.interfaces.presenters.items.activate_item_presenter \
    import ActivateItemPresenterInterface
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.validations.items.activate_item_validator \
    import ActivateItemInputDtoValidator
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException


class ActivateItemUseCase:
    """ Activate Item Use Case
    """

    def __init__(
        self,
        presenter: ActivateItemPresenterInterface,
        repository: ItemRepositoryInterface,
        logger: LoggerInterface,
    ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self, input_dto: ActivateItemInputDto) -> Dict:
        """ This method is responsible for activating an item
        :param input_dto: The input data
        :type input_dto: ActivateItemInputDto
        :return: Dict
        """
        validator = ActivateItemInputDtoValidator(input_dto.to_dict())
        validator.validate()
        item = self.repository.activate(input_dto.item_id)
        if item is None:
            self.logger.log_exception("Item not found")
            raise ItemNotFoundException("id", input_dto.item_id)
        output_dto = ActivateItemOutputDto(item)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Item Activated Successfully")
        return presenter_response
