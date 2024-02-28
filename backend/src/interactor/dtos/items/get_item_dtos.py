""" Module for Get Item Dtos
"""


from dataclasses import dataclass, asdict
from src.domain.entities.item import Item
from src.domain.value_objects import ItemId


@dataclass
class GetItemInputDto:
    """ Input Dto for get item
    """
    item_id: ItemId

    def to_dict(self):
        """ Convert to dictionary
        """
        return asdict(self)


@dataclass
class GetItemOutputDto:
    """ Output Dto for get item
    """
    item: Item
