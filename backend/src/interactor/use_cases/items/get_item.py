""" This module is responsible for retrieving an item
"""


from typing import Dict
from src.interactor.dtos.items.get_item_dtos \
    import GetItemInputDto, GetItemOutputDto
from src.interactor.interfaces.presenters.items.get_item_presenter \
    import GetItemPresenterInterface
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.validations.items.get_item_validator \
    import GetItemInputDtoValidator
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException


class GetItemUseCase:
    """ This class is responsible for retrieving an item
    """

    def __init__(
        self,
        presenter: GetItemPresenterInterface,
        repository: ItemRepositoryInterface,
        logger: LoggerInterface,
    ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self, input_dto: GetItemInputDto) -> Dict:
        """ This method is responsible for retrieving an item
        :param input_dto: The input data
        :type input_dto: GetItemInputDto
        :return: Dict
        """
        validator = GetItemInputDtoValidator(input_dto.to_dict())
        validator.validate()
        item = self.repository.get(input_dto.item_id)
        if item is None:
            self.logger.log_exception("Item not found")
            raise ItemNotFoundException(input_dto.item_id)
        output_dto = GetItemOutputDto(item)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Item Retrieved Successfully")
        return presenter_response
