# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from .delete_item_dtos import DeleteItemInputDto


def test_delete_item_input_dto_valid(fixture_item_biscuit):
    input_dto = DeleteItemInputDto(
        item_id = fixture_item_biscuit['item_id'],
    )
    assert input_dto.item_id == fixture_item_biscuit['item_id']
    assert input_dto.to_dict() == {
        "item_id": fixture_item_biscuit['item_id']
    }
