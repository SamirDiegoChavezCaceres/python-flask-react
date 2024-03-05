# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from .get_item_by_name_dtos import GetItemByNameInputDto


def test_get_item_by_name_input_dto_valid(fixture_item_biscuit):
    input_dto = GetItemByNameInputDto(
        name=fixture_item_biscuit['name']
    )
    assert input_dto.name == fixture_item_biscuit['name']
    assert input_dto.to_dict() == {
        "name": fixture_item_biscuit['name']
    }
