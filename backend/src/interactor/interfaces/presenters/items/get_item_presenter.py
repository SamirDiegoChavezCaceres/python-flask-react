""" Module for the GetItemPresenter interface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.items.get_item_dtos import GetItemOutputDto


class GetItemPresenterInterface(ABC):
    """ Class for the interface of the GetItemPresenter
    """
    @abstractmethod
    def present(self, output_dto: GetItemOutputDto) -> Dict:
        """ Present the item"""
