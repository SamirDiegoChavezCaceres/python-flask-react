# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from .update_item_dtos import UpdateItemInputDto


def test_update_item_input_dto_valid(fixture_item_biscuit):
    input_dto = UpdateItemInputDto(
        item_id=fixture_item_biscuit['item_id'],
        codebar=fixture_item_biscuit['codebar'],
        name=fixture_item_biscuit['name'],
        description=fixture_item_biscuit['description'],
        price=fixture_item_biscuit['price'],
        stock=fixture_item_biscuit['stock'],
        state=fixture_item_biscuit['state'],
    )
    assert input_dto.item_id == fixture_item_biscuit['item_id']
    assert input_dto.codebar == fixture_item_biscuit['codebar']
    assert input_dto.name == fixture_item_biscuit['name']
    assert input_dto.description == fixture_item_biscuit['description']
    assert input_dto.price == fixture_item_biscuit['price']
    assert input_dto.stock == fixture_item_biscuit['stock']
    assert input_dto.state == fixture_item_biscuit['state']
    assert input_dto.to_dict() == {
        "item_id": fixture_item_biscuit['item_id'],
        "codebar": fixture_item_biscuit['codebar'],
        "name": fixture_item_biscuit['name'],
        "description": fixture_item_biscuit['description'],
        "price": fixture_item_biscuit['price'],
        "stock": fixture_item_biscuit['stock'],
        "state": fixture_item_biscuit['state'],
    }
