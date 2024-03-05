# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.validations.items.get_item_by_name_validator \
    import GetItemByNameInputDtoValidator


def test_get_item_by_name_validator_valid_data(
        mocker,
        fixture_item_biscuit
):
    mocker.patch("src.interactor.validations.base_input_validator.\
BaseInputValidator.verify")
    input_data = {
        "name": fixture_item_biscuit["name"]
    }
    schema = {
        "name": {
            "empty": False,
            "required": True,
        }
    }
    validator = GetItemByNameInputDtoValidator(input_data)
    validator.validate()
    validator.verify.assert_called_once_with(schema) # pylint: disable=no-member


def test_base_validator_with_empty_data():
    data = {
        "name": ""
    }
    validator = GetItemByNameInputDtoValidator(data)
    with pytest.raises(ValueError) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Name: empty values not allowed"
