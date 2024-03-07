""" Module for the UpdateItemPresenter
"""


from typing import Dict
from src.interactor.dtos.items.update_item_dtos import UpdateItemOutputDto
from src.interactor.interfaces.presenters.items.update_item_presenter \
    import UpdateItemPresenterInterface



class UpdateItemPresenter(UpdateItemPresenterInterface):
    """ Presenter for UpdateItem
    """
    def present(self, output_dto: UpdateItemOutputDto) -> Dict:
        """ Method to present the output
        :param output_dto: UpdateItemOutputDto
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
