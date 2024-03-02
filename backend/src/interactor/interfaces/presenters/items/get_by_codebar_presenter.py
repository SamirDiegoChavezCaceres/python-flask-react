""" Module for the GetItemByCodebarPresenter interface
"""


from typing import Dict
from abc import ABC, abstractmethod
from src.interactor.dtos.items.get_by_codebar_dtos \
    import GetItemByCodebarOutputDto


class GetItemByCodebarPresenterInterface(ABC):
    """ Class for the interface of the GetItemByCodebarPresenter
    """
    @abstractmethod
    def present(self, output_dto: GetItemByCodebarOutputDto) -> Dict:
        """ Present the item """
