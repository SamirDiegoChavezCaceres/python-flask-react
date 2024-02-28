""" This module contains the UpdateItem use case.
"""


from typing import Dict
from src.interactor.dtos.items.update_item_dtos \
    import UpdateItemInputDto, UpdateItemOutputDto
from src.interactor.interfaces.presenters.items.update_item_presenter \
    import UpdateItemPresenterInterface
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.validations.items.update_item_validator \
    import UpdateItemInputDtoValidator
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException
from src.domain.entities.item import Item


class UpdateItemUseCase:
    """ This class is responsible for updating an item
    """

    def __init__(
        self,
        presenter: UpdateItemPresenterInterface,
        repository: ItemRepositoryInterface,
        logger: LoggerInterface,
    ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self, input_dto: UpdateItemInputDto) -> Dict:
        """ This method is responsible for updating an item
        :param input_dto: The input data
        :type input_dto: UpdateItemInputDto
        :return: Dict
        """
        validator = UpdateItemInputDtoValidator(input_dto.to_dict())
        validator.validate()
        item = self.repository.update(
            Item(
                input_dto.item_id,
                input_dto.codebar,
                input_dto.name,
                input_dto.description,
                input_dto.price,
                input_dto.stock,
                input_dto.state,
            )
        )
        if item is None:
            self.logger.log_exception("Item not found")
            raise ItemNotFoundException(input_dto.item_id)
        output_dto = UpdateItemOutputDto(item)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Item Saved Successfully")
        return presenter_response
