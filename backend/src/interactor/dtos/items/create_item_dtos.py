""" Module for Create Item Dtos
"""


from dataclasses import dataclass, asdict
from src.domain.entities.item import Item


@dataclass
class CreateItemInputDto:
    """ Input Dto for create item
    """
    codebar: str
    name: str
    description: str
    price: float
    stock: int

    def to_dict(self):
        """ Convert to dictionary
        """
        return asdict(self)
    

@dataclass
class CreateItemOutputDto:
    """ Output Dto for create item
    """
    item: Item
