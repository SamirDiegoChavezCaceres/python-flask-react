""" Module for the DeactivateItemPresenter interface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.items.delete_item_dtos import DeleteItemOutputDto


class DeleteItemPresenterInterface(ABC):
    """ Class for the interface of the DeleteItemPresenter
    """
    @abstractmethod
    def present(self, output_dto: DeleteItemOutputDto) -> Dict:
        """ Present the item"""
