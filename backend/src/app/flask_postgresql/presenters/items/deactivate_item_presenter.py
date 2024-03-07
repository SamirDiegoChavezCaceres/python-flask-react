""" Module for the DeactivateItemPresenter
"""


from typing import Dict
from src.interactor.dtos.items.deactivate_item_dtos \
    import DeactivateItemOutputDto
from src.interactor.interfaces.presenters.items.deactivate_item_presenter \
    import DeactivateItemPresenterInterface


class DeactivateItemPresenter(DeactivateItemPresenterInterface):
    """ Presenter for DeactivateItem
    """
    def present(self, output_dto: DeactivateItemOutputDto) -> Dict:
        """ Method to present the output
        :param output_dto: DeactivateItemOutputDto
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
