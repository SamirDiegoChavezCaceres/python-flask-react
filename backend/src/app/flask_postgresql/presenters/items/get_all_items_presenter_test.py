# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from src.interactor.dtos.items.get_all_items_dtos import GetAllItemsOutputDto
from src.domain.entities.item import Item
from .get_all_items_presenter import GetAllItemsPresenter


def test_get_all_items_presenter(fixture_item_biscuit, fixture_item_chocolate):
    item_biscuit = Item(
        item_id=fixture_item_biscuit["item_id"],
        codebar=fixture_item_biscuit["codebar"],
        name=fixture_item_biscuit["name"],
        description=fixture_item_biscuit["description"],
        price=fixture_item_biscuit["price"],
        stock=fixture_item_biscuit["stock"],
        state=fixture_item_biscuit["state"]
    )
    item_chocolate = Item(
        item_id=fixture_item_chocolate["item_id"],
        codebar=fixture_item_chocolate["codebar"],
        name=fixture_item_chocolate["name"],
        description=fixture_item_chocolate["description"],
        price=fixture_item_chocolate["price"],
        stock=fixture_item_chocolate["stock"],
        state=fixture_item_chocolate["state"]
    )
    output_dto = GetAllItemsOutputDto([item_biscuit, item_chocolate])
    presenter = GetAllItemsPresenter()
    assert presenter.present(output_dto) == {
        "items": [
            {
                "item_id": fixture_item_biscuit["item_id"],
                "codebar": fixture_item_biscuit["codebar"],
                "name": fixture_item_biscuit["name"],
                "description": fixture_item_biscuit["description"],
                "price": fixture_item_biscuit["price"],
                "stock": fixture_item_biscuit["stock"],
                "state": fixture_item_biscuit["state"]
            },
            {
                "item_id": fixture_item_chocolate["item_id"],
                "codebar": fixture_item_chocolate["codebar"],
                "name": fixture_item_chocolate["name"],
                "description": fixture_item_chocolate["description"],
                "price": fixture_item_chocolate["price"],
                "stock": fixture_item_chocolate["stock"],
                "state": fixture_item_chocolate["state"]
            }
        ]
    }
