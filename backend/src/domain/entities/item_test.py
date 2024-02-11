# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from .item import Item


def test_item_creation(fixture_item_biscuit):
    item = Item(
        fixture_item_biscuit["item_id"],
        fixture_item_biscuit["codebar"],
        fixture_item_biscuit["name"],
        fixture_item_biscuit["description"],
        fixture_item_biscuit["price"],
        fixture_item_biscuit["stock"],
        fixture_item_biscuit["state"],
    )
    assert item.item_id == fixture_item_biscuit["item_id"]
    assert item.codebar == fixture_item_biscuit["codebar"]
    assert item.name == fixture_item_biscuit["name"]
    assert item.description == fixture_item_biscuit["description"]
    assert item.price == fixture_item_biscuit["price"]
    assert item.stock == fixture_item_biscuit["stock"]
    assert item.state == fixture_item_biscuit["state"]


def test_item_from_dict(fixture_item_biscuit):
    item = Item.from_dict(fixture_item_biscuit)
    assert item.to_dict() == fixture_item_biscuit


def test_item_comparison(fixture_item_biscuit):
    item1 = Item.from_dict(fixture_item_biscuit)
    item2 = Item.from_dict(fixture_item_biscuit)
    assert item1 == item2
    