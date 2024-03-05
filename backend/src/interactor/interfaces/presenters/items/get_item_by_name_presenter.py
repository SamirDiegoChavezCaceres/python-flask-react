""" Module for the GetItemByNamePresenter interface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.items.get_item_by_name_dtos \
    import GetItemByNameOutputDto


class GetItemByNamePresenterInterface(ABC):
    """ Class for the interface of the GetItemByNamePresenter
    """
    @abstractmethod
    def present(self, output_dto: GetItemByNameOutputDto) -> Dict:
        """ Present the item"""
