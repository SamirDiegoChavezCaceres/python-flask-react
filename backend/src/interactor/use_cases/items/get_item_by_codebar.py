""" This module is responsible for retrieving an item by codebar
"""


from typing import Dict
from src.interactor.dtos.items.get_by_codebar_dtos \
    import GetItemByCodebarInputDto, GetItemByCodebarOutputDto
from src.interactor.interfaces.presenters.items.get_by_codebar_presenter \
    import GetItemByCodebarPresenterInterface
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.validations.items.get_by_codebar_validator \
    import GetItemByCodebarInputDtoValidator
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException


class GetItemByCodebarUseCase:
    """ This class is responsible for retrieving an item by codebar
    """

    def __init__(
        self,
        presenter: GetItemByCodebarPresenterInterface,
        repository: ItemRepositoryInterface,
        logger: LoggerInterface,
    ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self, input_dto: GetItemByCodebarInputDto) -> Dict:
        """ This method is responsible for retrieving an item by codebar
        :param input_dto: The input data
        :type input_dto: GetItemInputDto
        :return: Dict
        """
        validator = GetItemByCodebarInputDtoValidator(input_dto.to_dict())
        validator.validate()
        item = self.repository.get_by_codebar(input_dto.codebar)
        if item is None:
            self.logger.log_exception("Item not found")
            raise ItemNotFoundException("codebar", input_dto.codebar)
        output_dto = GetItemByCodebarOutputDto(item)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Item Retrieved Successfully")
        return presenter_response
