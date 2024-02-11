""" This module has defined the Item entity.
"""


from dataclasses import dataclass, asdict
from src.domain.value_objects import ItemId


@dataclass
class Item:
    """This class represents an Item entity.
    """
