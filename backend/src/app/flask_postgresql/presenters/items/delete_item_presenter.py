""" Module for the DeleteItemPresenter
"""


from typing import Dict
from src.interactor.dtos.items.delete_item_dtos import DeleteItemOutputDto
from src.interactor.interfaces.presenters.items.delete_item_presenter \
    import DeleteItemPresenterInterface



class DeleteItemPresenter(DeleteItemPresenterInterface):
    """ Presenter for DeleteItem
    """
    def present(self, output_dto: DeleteItemOutputDto) -> Dict:
        """ Method to present the output
        :param output_dto: DeleteItemOutputDto
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
