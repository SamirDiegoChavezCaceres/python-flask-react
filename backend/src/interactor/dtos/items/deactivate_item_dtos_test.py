# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from .deactivate_item_dtos import DeactivateItemInputDto


def test_deactivate_item_input_dto_valid(fixture_item_biscuit):
    input_dto = DeactivateItemInputDto(
        item_id = fixture_item_biscuit['item_id'],
    )
    assert input_dto.item_id == fixture_item_biscuit['item_id']
    assert input_dto.to_dict() == {
        "item_id": fixture_item_biscuit['item_id']
    }
