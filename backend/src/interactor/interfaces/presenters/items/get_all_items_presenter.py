""" Module for the Get All Items Presenter interface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.items.get_all_items_dtos import GetAllItemsOutputDto


class GetAllItemsPresenterInterface(ABC):
    """ Class for the interface of the GetAllItemsPresenter
    """
    @abstractmethod
    def present(self, output_dto: GetAllItemsOutputDto) -> Dict:
        """ Present the items"""
