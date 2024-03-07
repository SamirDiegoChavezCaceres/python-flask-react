""" Module for the GetItemByNamePresenter
"""


from typing import Dict
from src.interactor.dtos.items.get_item_by_name_dtos \
    import GetItemByNameOutputDto
from src.interactor.interfaces.presenters.items.get_item_by_name_presenter \
    import GetItemByNamePresenterInterface


class GetItemByNamePresenter(GetItemByNamePresenterInterface):
    """ Presenter for GetItemByName
    """
    def present(self, output_dto: GetItemByNameOutputDto) -> Dict:
        """ Method to present the output
        :param output_dto: GetItemByNameOutputDto
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
