# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.validations.items.get_item_validator \
    import GetItemInputDtoValidator
from src.interactor.errors.error_classes import FieldValueNotPermittedException


def test_get_item_validator_valid_data(
        mocker,
        fixture_item_biscuit
):
    mocker.patch("src.interactor.validations.base_input_validator.\
BaseInputValidator.verify")
    input_data = {
        "item_id": fixture_item_biscuit["item_id"]
    }
    schema = {
        "item_id": {
            "empty": False,
            "required": True,
        }
    }
    validator = GetItemInputDtoValidator(input_data)
    validator.validate()
    validator.verify.assert_called_once_with(schema) # pylint: disable=no-member


def test_base_validator_with_empty_data():
    data = {
        "item_id": ""
    }
    validator = GetItemInputDtoValidator(data)
    with pytest.raises(ValueError) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Item_id: empty values not allowed"
