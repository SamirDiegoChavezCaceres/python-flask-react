""" Module for Get Item by Name Dtos
"""


from dataclasses import dataclass, asdict
from src.domain.entities.item import Item


@dataclass
class GetItemByNameInputDto:
    """ Input Dto for get item by name
    """
    name: str

    def to_dict(self):
        """ Convert to dictionary
        """
        return asdict(self)


@dataclass
class GetItemByNameOutputDto:
    """ Output Dto for get item by name
    """
    item: Item
