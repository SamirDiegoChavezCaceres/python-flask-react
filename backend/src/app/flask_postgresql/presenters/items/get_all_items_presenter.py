""" Module for the GetAllItemsPresenter
"""


from typing import Dict
from src.interactor.dtos.items.get_all_items_dtos import GetAllItemsOutputDto
from src.interactor.interfaces.presenters.items.get_all_items_presenter \
    import GetAllItemsPresenterInterface


class GetAllItemsPresenter(GetAllItemsPresenterInterface):
    """ Presenter for GetAllItems
    """
    def present(self, output_dto: GetAllItemsOutputDto) -> Dict:
        """ Method to present the output
        :param output_dto: GetAllItemsOutputDto
        :return: Dict
        """
        items = []
        for item in output_dto.items:
            items.append({
                "item_id": item.item_id,
                "codebar": item.codebar,
                "name": item.name,
                "description": item.description,
                "price": item.price,
                "stock": item.stock,
                "state": item.state
            })
        return {
            "items": items
        }
