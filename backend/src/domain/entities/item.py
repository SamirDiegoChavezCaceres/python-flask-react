""" This module has defined the Item entity.
"""


from dataclasses import dataclass, asdict
from src.domain.value_objects import ItemId


@dataclass
class Item:
    """This class represents an Item entity.
    """
    item_id: ItemId
    codebar: str
    name: str
    description: str
    price: float
    stock: int
    state: bool

    @classmethod
    def from_dict(cls, data):
        """ Convert data from a dictionary
        """
        return cls(**data)

    def to_dict(self):
        """ Convert data to a dictionary
        """
        return asdict(self)
    