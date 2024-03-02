# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from .get_item_dtos import GetItemInputDto


def test_get_item_input_dto_valid(fixture_item_biscuit):
    input_dto = GetItemInputDto(
        item_id=fixture_item_biscuit['item_id']
    )
    assert input_dto.item_id == fixture_item_biscuit['item_id']
    assert input_dto.to_dict() == {
        "item_id": fixture_item_biscuit['item_id']
    }
