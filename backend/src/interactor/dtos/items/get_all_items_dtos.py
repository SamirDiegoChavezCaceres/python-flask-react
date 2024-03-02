""" Module for Get All Items Dtos
"""


from dataclasses import dataclass
from typing import List
from src.domain.entities.item import Item


@dataclass
class GetAllItemsOutputDto:
    """ Output Dto for get all items
    """
    items: List[Item]
