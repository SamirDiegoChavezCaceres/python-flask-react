""" Defines the professions detabase model.
"""


import uuid
from dataclasses import dataclass, asdict
from src.infra.db_models.mongodb.mongodb_base import Base


@dataclass
class ItemsDBModel(Base):
    """Items database model.
    """

    __tablename__ = "items"

    _id: str
    codebar: str
    name: str
    description: str
    price: float
    stock: int
    state: bool = True

    def to_dict(self):
        """ Convert to dictionary
        """
        return asdict(self)
