""" Module Get Item By Name Use Case
"""


from typing import Dict
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.interfaces.presenters.items.get_item_by_name_presenter \
    import GetItemByNamePresenterInterface
from src.interactor.dtos.items.get_item_by_name_dtos \
    import GetItemByNameInputDto, GetItemByNameOutputDto
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException
from src.interactor.validations.items.get_item_by_name_validator \
    import GetItemByNameInputDtoValidator


class GetItemByNameUseCase:
    """ This class is responsible for retrieving an item by name
    """

    def __init__(
        self,
        presenter: GetItemByNamePresenterInterface,
        repository: ItemRepositoryInterface,
        logger: LoggerInterface,
    ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self, input_dto: GetItemByNameInputDto) -> Dict:
        """ This method is responsible for retrieving an item by name
        :param input_dto: The input data
        :type input_dto: GetItemByNameInputDto
        :return: Dict
        """
        validator = GetItemByNameInputDtoValidator(input_dto.to_dict())
        validator.validate()
        item = self.repository.get_by_name(input_dto.name)
        if item is None:
            self.logger.log_exception("Item not found")
            raise ItemNotFoundException("name", input_dto.name)
        output_dto = GetItemByNameOutputDto(item)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Item Retrieved Successfully")
        return presenter_response
