# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


from typing import Dict
import pytest
from src.interactor.validations.base_input_validator import BaseInputValidator


class BaseValidator(BaseInputValidator):
    def __init__(self, data: Dict):
        super().__init__(data)
        self.schema = {
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

    def validate(self):
        super().verify(self.schema)


def test_base_validator_with_valid_data():
    data = {
        "codebar": "1234567890",
        "name": "Test",
        "description": "Test",
        "price": 1.0,
        "stock": 1,
        "state": True,
    }
    validator = BaseValidator(data)
    assert validator.validate() is None


def test_base_validator_with_small_data():
    data = {
        "codebar": "1",
        "name": "T",
        "description": "T",
        "price": 1.0,
        "stock": 1,
        "state": True,
    }
    validator = BaseValidator(data)
    with pytest.raises(ValueError) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Description: min length is 3\n\
Name: min length is 3"


def test_base_validator_with_long_data():
    data = {
        "codebar": "1" * 21,
        "name": "Test",
        "description": "Test",
        "price": 1.0,
        "stock": 1,
        "state": True,
    }
    validator = BaseValidator(data)
    with pytest.raises(ValueError) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Codebar: max length is 20"


def test_base_validator_with_empty_data():
    data = {
        "codebar": "",
        "name": "Test",
        "description": "Test",
        "price": 1.0,
        "stock": 1,
        "state": True,
    }
    validator = BaseValidator(data)
    with pytest.raises(ValueError) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Codebar: empty values not allowed"


def test_base_validator_with_required_data():
    data = {
        "description": "Test",
        "price": 1.0,
        "stock": 1,
        "state": True,
    }
    validator = BaseValidator(data)
    with pytest.raises(ValueError) as excinfo:
        validator.validate()
    assert str(excinfo.value) == "Name: required field"
