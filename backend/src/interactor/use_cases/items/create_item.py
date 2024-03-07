""" This module is responsible for creating 
"""


from typing import Dict
from src.interactor.dtos.items.create_item_dtos \
    import CreateItemInputDto, CreateItemOutputDto
from src.interactor.interfaces.presenters.items.create_item_presenter \
    import CreateItemPresenterInterface
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.validations.items.create_item_validator \
    import CreateItemInputDtoValidator
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotCreatedException


class CreateItemUseCase:
    """ This class is responsible for creating a new item
    """

    def __init__(
        self,
        presenter: CreateItemPresenterInterface,
        repository: ItemRepositoryInterface,
        logger: LoggerInterface,
    ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self, input_dto: CreateItemInputDto) -> Dict:
        """ This method is responsible for creating a new item
        :param input_dto: The input data
        :type input_dto: CreateItemInputDto
        :return: Dict
        """
        validator = CreateItemInputDtoValidator(input_dto.to_dict())
        validator.validate()
        item = self.repository.create(
            input_dto.codebar,
            input_dto.name,
            input_dto.description,
            input_dto.price,
            input_dto.stock,
        )
        if item is None:
            self.logger.log_exception("Item creation failed")
            raise ItemNotCreatedException(input_dto.name, "Item")
        output_dto = CreateItemOutputDto(item)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Item Created Successfully")
        return presenter_response
