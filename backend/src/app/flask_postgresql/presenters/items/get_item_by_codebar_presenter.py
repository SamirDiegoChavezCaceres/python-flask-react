""" Module for the GetItemByCodebarPresenter
"""


from typing import Dict
from src.interactor.dtos.items.get_by_codebar_dtos \
    import GetItemByCodebarOutputDto
from src.interactor.interfaces.presenters.items.get_by_codebar_presenter \
    import GetItemByCodebarPresenterInterface


class GetItemByCodebarPresenter(GetItemByCodebarPresenterInterface):
    """ Presenter for GetItemByCodebar
    """
    def present(self, output_dto: GetItemByCodebarOutputDto) -> Dict:
        """ Method to present the output
        :param output_dto: GetItemByCodebarOutputDto
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
