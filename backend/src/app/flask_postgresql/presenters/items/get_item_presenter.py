""" Module for the GetItemPresenter
"""


from typing import Dict
from src.interactor.dtos.items.get_item_dtos import GetItemOutputDto
from src.interactor.interfaces.presenters.items.get_item_presenter \
    import GetItemPresenterInterface


class GetItemPresenter(GetItemPresenterInterface):
    """ Presenter for GetItem
    """
    def present(self, output_dto: GetItemOutputDto) -> Dict:
        """ Method to present the output
        :param output_dto: GetItemOutputDto
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
