""" This module is responsible for deleting an item
"""


from typing import Dict
from src.interactor.dtos.items.delete_item_dtos \
    import DeleteItemInputDto, DeleteItemOutputDto
from src.interactor.interfaces.presenters.items.delete_item_presenter \
    import DeleteItemPresenterInterface
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.validations.items.delete_item_validator \
    import DeleteItemInputDtoValidator
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException


class DeleteItemUseCase:
    """ Delete Item Use Case
    """

    def __init__(
        self,
        presenter: DeleteItemPresenterInterface,
        repository: ItemRepositoryInterface,
        logger: LoggerInterface,
    ) -> None:
        self.presenter = presenter
        self.repository = repository
        self.logger = logger

    def execute(self, input_dto: DeleteItemInputDto) -> Dict:
        """ This method is responsible for deleting an item
        :param input_dto: The input data
        :type input_dto: DeleteItemInputDto
        :return: Dict
        """
        validator = DeleteItemInputDtoValidator(input_dto.to_dict())
        validator.validate()
        item = self.repository.delete(input_dto.item_id)
        if item is None:
            self.logger.log_exception("Item not found")
            raise ItemNotFoundException("id", input_dto.item_id)
        output_dto = DeleteItemOutputDto(item)
        presenter_response = self.presenter.present(output_dto)
        self.logger.log_info("Item Deleted Successfully")
        return presenter_response
