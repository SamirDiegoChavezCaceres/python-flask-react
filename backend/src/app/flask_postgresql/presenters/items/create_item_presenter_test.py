# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from src.interactor.dtos.items.create_item_dtos import CreateItemOutputDto
from src.domain.entities.item import Item
from .create_item_presenter import CreateItemPresenter


def test_create_item_presenter(fixture_item_biscuit):
    item = Item(
        item_id=fixture_item_biscuit["item_id"],
        codebar=fixture_item_biscuit["codebar"],
        name=fixture_item_biscuit["name"],
        description=fixture_item_biscuit["description"],
        price=fixture_item_biscuit["price"],
        stock=fixture_item_biscuit["stock"],
        state=fixture_item_biscuit["state"]
    )
    output_dto = CreateItemOutputDto(item)
    presenter = CreateItemPresenter()
    assert presenter.present(output_dto) == {
        "item_id": fixture_item_biscuit["item_id"],
        "codebar": fixture_item_biscuit["codebar"],
        "name": fixture_item_biscuit["name"],
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"],
        "state": fixture_item_biscuit["state"]
    }
