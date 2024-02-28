# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.validations.items.update_item_validator \
    import UpdateItemInputDtoValidator
from src.interactor.errors.error_classes import FieldValueNotPermittedException


def test_update_item_validator_valid_data(
        mocker,
        fixture_item_biscuit
):
    mocker.patch("src.interactor.validations.base_input_validator.\
BaseInputValidator.verify")
    input_data = {
            "item_id": fixture_item_biscuit["item_id"],
            "codebar": fixture_item_biscuit["codebar"],
            "name": fixture_item_biscuit["name"],
            "description": fixture_item_biscuit["description"],
            "price": fixture_item_biscuit["price"],
            "stock": fixture_item_biscuit["stock"],
            "state": fixture_item_biscuit["state"],
    }
    schema = {
            "item_id": {
                "empty": False,
            },
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
    validator = UpdateItemInputDtoValidator(input_data)
    validator.validate()
    validator.verify.assert_called_once_with(schema)  # pylint: disable=E1101


def test_base_validator_with_empty_data():
    data = {
        "item_id": "",
        "codebar": "codebar",
        "name": "Test",
        "description": "Test",
        "price": 1.0,
        "stock": 1,
        "state": True,
    }
    validator = UpdateItemInputDtoValidator(data)
    with pytest.raises(ValueError) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Item_id: empty values not allowed"


def test_update_item_custom_validation(fixture_item_biscuit):
    data = {
        "item_id": fixture_item_biscuit["item_id"],
        "codebar": "1234567890",
        "name": "Item",
        "description": "Item",
        "price": 1.0,
        "stock": 1,
        "state": True,
    }
    validator = UpdateItemInputDtoValidator(data)
    with pytest.raises(FieldValueNotPermittedException) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Name: Item is not permitted"
