""" Module for the CreateItemPresenter interface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.items.create_item_dtos import CreateItemOutputDto


class CreateItemPresenterInterface(ABC):
    """ Class for the interface of the CreateItemPresenter
    """
    @abstractmethod
    def present(self, output_dto: CreateItemOutputDto) -> Dict:
        """ Present the item"""
