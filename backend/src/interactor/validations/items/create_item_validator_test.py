# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.validations.items.create_item_validator \
    import CreateItemInputDtoValidator
from src.interactor.errors.error_classes import FieldValueNotPermittedException


def test_create_item_validator_valid_data(
        mocker,
        fixture_item_biscuit
):
    mocker.patch("src.interactor.validations.base_input_validator.\
BaseInputValidator.verify")
    input_data = {
            "codebar": fixture_item_biscuit["codebar"],
            "name": fixture_item_biscuit["name"],
            "description": fixture_item_biscuit["description"],
            "price": fixture_item_biscuit["price"],
            "stock": fixture_item_biscuit["stock"],
            "state": fixture_item_biscuit["state"],
    }
    schema = {
            "codebar": {
                "type": "string",
                "maxlength": 20,
                "empty": False,
            },
            "name": {
                "type": "string",
                "minlength": 3,
                "maxlength": 25,
                "required": True,
                "empty": False,
            },
            "description": {
                "type": "string",
                "minlength": 3,
                "maxlength": 200,
                "required": True,
                "empty": False,
            },
            "price": {
                "type": "number",
                "required": True,
            },
            "stock": {
                "type": "integer",
                "required": True,
            },
            "state": {
                "type": "boolean",
                "required": True,
            },
    }
    validator = CreateItemInputDtoValidator(input_data)
    validator.validate()
    validator.verify.assert_called_once_with(schema)  # pylint: disable=E1101


def test_base_validator_with_empty_data():
    data = {
        "codebar": "",
        "name": "Test",
        "description": "Test",
        "price": 1.0,
        "stock": 1,
        "state": True,
    }
    validator = CreateItemInputDtoValidator(data)
    with pytest.raises(ValueError) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Codebar: empty values not allowed"


def test_create_item_custom_validation(fixture_item_biscuit):
    data = {
        "codebar": "1234567890",
        "name": "Item",
        "description": "Test",
        "price": 1.0,
        "stock": 1,
        "state": True,
    }
    validator = CreateItemInputDtoValidator(data)
    with pytest.raises(FieldValueNotPermittedException) as exception_info:
        validator.validate()
    assert str(exception_info.value) == "Name: Item is not permitted"
