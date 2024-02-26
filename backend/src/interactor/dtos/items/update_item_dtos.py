""" Module for Update Item Dtos
"""


from dataclasses import dataclass, asdict
from src.domain.entities.item import Item


@dataclass
class UpdateItemInputDto:
    """ Input Dto for update item
    """
    item_id: str
    codebar: str
    name: str
    description: str
    price: float
    stock: int
    state: bool

    def to_dict(self):
        """ Convert to dictionary
        """
        return asdict(self)


@dataclass
class UpdateItemOutputDto:
    """ Output Dto for update item
    """
    item: Item
