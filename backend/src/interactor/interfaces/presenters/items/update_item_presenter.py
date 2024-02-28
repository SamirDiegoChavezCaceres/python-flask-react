""" Module for the UpdateItemPresenter interface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.items.update_item_dtos import  UpdateItemOutputDto


class UpdateItemPresenterInterface(ABC):
    """ Class for the interface of the UpdateItemPresenter
    """
    @abstractmethod
    def present(self, output_dto: UpdateItemOutputDto) -> Dict:
        """ Present the item"""
