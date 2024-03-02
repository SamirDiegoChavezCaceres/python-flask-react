# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.validations.items.get_by_codebar_validator \
    import GetItemByCodebarInputDtoValidator


def test_get_by_codebar_validator_valid_data(
        mocker,
        fixture_item_biscuit
):
    mocker.patch("src.interactor.validations.base_input_validator.\
BaseInputValidator.verify")
    input_data = {
        "codebar": fixture_item_biscuit["codebar"]
    }
    schema = {
        "codebar": {
            "empty": False,
            "required": True,
        }
    }
    validator = GetItemByCodebarInputDtoValidator(input_data)
    validator.validate()
    validator.verify.assert_called_once_with(schema) # pylint: disable=no-member


def test_base_validator_with_empty_data():
    data = {
        "codebar": ""
    }
    validator = GetItemByCodebarInputDtoValidator(data)
    with pytest.raises(ValueError) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Codebar: empty values not allowed"
