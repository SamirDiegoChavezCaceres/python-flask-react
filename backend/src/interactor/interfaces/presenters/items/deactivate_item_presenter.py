""" Module for the DeactivateItemPresenter interface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.items.deactivate_item_dtos import DeactivateItemOutputDto


class DeactivateItemPresenterInterface(ABC):
    """ Class for the interface of the DeactivateItemPresenter
    """
    @abstractmethod
    def present(self, output_dto: DeactivateItemOutputDto) -> Dict:
        """ Present the item"""
