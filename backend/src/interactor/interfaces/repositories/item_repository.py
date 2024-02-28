""" This module contains the interface for the ItemRepository.
"""


from abc import ABC, abstractmethod
from typing import Optional
from src.domain.value_objects import ItemId
from src.domain.entities.item import Item


class ItemRepositoryInterface(ABC):
    """ This class is the interface for the ItemRepository
    """
    @abstractmethod
    def get(self, item_id: ItemId) -> Optional[Item]:
        """ Get an item by id
        :param item_id: The id of the item
        :return: The item
        """

    @abstractmethod
    def create(
                self,
                codebar: str,
                name: str,
                description: str,
                price: float,
                stock: int,
    ) -> Optional[Item]:
        """ Create an item
        :param codebar: The codebar of the item
        :param name: The name of the item
        :param description: The description of the item
        :param price: The price of the item
        :param stock: The stock of the item
        :param state: The state of the item
        :return: The item
        """

    @abstractmethod
    def update(
                self,
                item: Item
    ) -> Optional[Item]:
        """ Update an item
        :param item: The item
        :return: The item updated
        """

    @abstractmethod
    def delete(self, item_id: ItemId) -> Optional[Item]:
        """ Delete an item
        :param item_id: The id of the item
        :return: The item
        """

    @abstractmethod
    def get_all(self) -> list[Item]:
        """ Get all items
        :return: The items
        """

    @abstractmethod
    def get_by_codebar(self, codebar: str) -> Optional[Item]:
        """ Get an item by codebar
        :param codebar: The codebar of the item
        :return: The item
        """

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[Item]:
        """ Get an item by name
        :param name: The name of the item
        :return: The item
        """

    @abstractmethod
    def activate(self, item_id: ItemId) -> Optional[Item]:
        """ Activate an item
        :param item_id: The id of the item
        :return: The item
        """

    @abstractmethod
    def deactivate(self, item_id: ItemId) -> Optional[Item]:
        """ Deactivate an item
        :param item_id: The id of the item
        :return: The item
        """
