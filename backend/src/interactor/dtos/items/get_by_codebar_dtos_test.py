# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from .get_by_codebar_dtos import GetItemByCodebarInputDto


def test_get_by_codebar_input_dto_valid(fixture_item_biscuit):
    input_dto = GetItemByCodebarInputDto(
        codebar=fixture_item_biscuit['codebar']
    )
    assert input_dto.codebar == fixture_item_biscuit['codebar']
    assert input_dto.to_dict() == {
        "codebar": fixture_item_biscuit['codebar']
    }
