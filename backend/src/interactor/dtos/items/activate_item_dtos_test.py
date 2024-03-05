# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from .activate_item_dtos import ActivateItemInputDto


def test_activate_item_input_dto_valid(fixture_item_biscuit):
    input_dto = ActivateItemInputDto(
        item_id = fixture_item_biscuit['item_id'],
    )
    assert input_dto.item_id == fixture_item_biscuit['item_id']
    assert input_dto.to_dict() == {
        "item_id": fixture_item_biscuit['item_id']
    }
