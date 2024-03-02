""" Module for Get Item Dtos by codebar
"""


from dataclasses import dataclass, asdict
from src.domain.entities.item import Item


@dataclass
class GetItemByCodebarInputDto:
    """ Input Dto for get item by codebar
    """
    codebar: str

    def to_dict(self):
        """ Convert to dictionary
        """
        return asdict(self)


@dataclass
class GetItemByCodebarOutputDto:
    """ Output Dto for get item by codebar
    """
    item: Item
