""" Module for the ActivateItemPresenter
"""


from typing import Dict
from src.interactor.dtos.items.activate_item_dtos import ActivateItemOutputDto
from src.interactor.interfaces.presenters.items.activate_item_presenter \
    import ActivateItemPresenterInterface


class ActivateItemPresenter(ActivateItemPresenterInterface):
    """ Presenter for ActivateItem
    """
    def present(self, output_dto: ActivateItemOutputDto) -> Dict:
        """ Method to present the output
        :param output_dto: ActivateItemOutputDto
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
