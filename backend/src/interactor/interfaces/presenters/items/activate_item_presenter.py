""" Module for the ActivateItemPresenter interface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.items.activate_item_dtos import ActivateItemOutputDto


class ActivateItemPresenterInterface(ABC):
    """ Class for the interface of the ActivateItemPresenter
    """
    @abstractmethod
    def present(self, output_dto: ActivateItemOutputDto) -> Dict:
        """ Present the item"""
