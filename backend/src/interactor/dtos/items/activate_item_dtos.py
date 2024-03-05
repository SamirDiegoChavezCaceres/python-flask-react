""" Module for Activate Item Dtos
"""


from dataclasses import dataclass, asdict
from src.domain.entities.item import Item
from src.domain.value_objects import ItemId


@dataclass
class ActivateItemInputDto:
    """ Input Dto for activate item
    """
    item_id: ItemId

    def to_dict(self):
        """ Convert to dictionary
        """
        return asdict(self)


@dataclass
class ActivateItemOutputDto:
    """ Output Dto for activate item
    """
    item: Item
