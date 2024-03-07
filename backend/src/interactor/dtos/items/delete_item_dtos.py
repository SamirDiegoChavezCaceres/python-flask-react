""" Module for Deactivate Item Dtos
"""


from dataclasses import dataclass, asdict
from src.domain.entities.item import Item
from src.domain.value_objects import ItemId


@dataclass
class DeleteItemInputDto:
    """ Input Dto for deactivate item
    """
    item_id: ItemId

    def to_dict(self):
        """ Convert to dictionary
        """
        return asdict(self)


@dataclass
class DeleteItemOutputDto:
    """ Output Dto for deactivate item
    """
    item: Item
