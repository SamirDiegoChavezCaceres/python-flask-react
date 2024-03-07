# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from src.interactor.dtos.items.get_item_by_name_dtos \
    import GetItemByNameOutputDto
from src.domain.entities.item import Item
from .get_item_by_name_presenter import GetItemByNamePresenter


def test_get_item_by_name_presenter(fixture_item_biscuit):
    item = Item(
        item_id=fixture_item_biscuit["item_id"],
        codebar=fixture_item_biscuit["codebar"],
        name=fixture_item_biscuit["name"],
        description=fixture_item_biscuit["description"],
        price=fixture_item_biscuit["price"],
        stock=fixture_item_biscuit["stock"],
        state=fixture_item_biscuit["state"]
    )
    output_dto = GetItemByNameOutputDto(item)
    presenter = GetItemByNamePresenter()
    assert presenter.present(output_dto) == {
        "item_id": fixture_item_biscuit["item_id"],
        "codebar": fixture_item_biscuit["codebar"],
        "name": fixture_item_biscuit["name"],
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"],
        "state": fixture_item_biscuit["state"]
    }
