# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from src.interactor.errors.error_classes \
    import FieldValueNotPermittedException
from src.interactor.errors.error_classes import ItemNotCreatedException
from src.interactor.errors.error_classes import UniqueViolationError
from src.interactor.errors.error_classes import ItemNotFoundException
from src.interactor.errors.error_classes import ItemsNotFoundException

def test_value_not_permitted_exception():
    with pytest.raises(FieldValueNotPermittedException) as exception_info:
        raise FieldValueNotPermittedException("name", "Item")
    assert str(exception_info.value) == "Name: Item is not permitted"


def test_item_not_created_exception():
    with pytest.raises(ItemNotCreatedException) as exception_info:
        raise ItemNotCreatedException("item name", "item")
    assert str(exception_info.value) == \
        "Item 'item name' was not created correctly"


def test_unique_violation_error():
    with pytest.raises(UniqueViolationError) as exception_info:
        raise UniqueViolationError("item", "name", "item name")
    assert str(exception_info.value) == \
        "Item with name: 'item name' already exists"


def test_item_not_found_exception():
    with pytest.raises(ItemNotFoundException) as exception_info:
        raise ItemNotFoundException("item id")
    assert str(exception_info.value) == "Item with id: item id not found"


def test_items_not_found_exception():
    with pytest.raises(ItemsNotFoundException) as exception_info:
        raise ItemsNotFoundException()
    assert str(exception_info.value) == "Items not found"
