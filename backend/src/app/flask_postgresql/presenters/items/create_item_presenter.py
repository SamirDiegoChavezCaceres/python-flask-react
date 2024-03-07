""" Module for the CreateItemPresenter
"""


from typing import Dict
from src.interactor.dtos.items.create_item_dtos import CreateItemOutputDto
from src.interactor.interfaces.presenters.items.create_item_presenter \
    import CreateItemPresenterInterface


class CreateItemPresenter(CreateItemPresenterInterface):
    """ Presenter for CreateItem
    """
    def present(self, output_dto: CreateItemOutputDto) -> Dict:
        """ Method to present the output
        :param output_dto: CreateItemOutputDto
        :return: Dict
        """
        return {
            "item_id": output_dto.item.item_id,
            "codebar": output_dto.item.codebar,
            "name": output_dto.item.name,
            "description": output_dto.item.description,
            "price": output_dto.item.price,
            "stock": output_dto.item.stock,
            "state": output_dto.item.state
        }
