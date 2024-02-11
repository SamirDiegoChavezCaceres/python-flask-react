""" This module contains the interface for the ItemRepository.
"""


from abc import ABC, abstractmethod
from typing import Optional
from src.domain.value_objects import ItemId
from src.domain.entities.item import Item