# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import uuid
import pytest


@pytest.fixture
def fixture_item_biscuit():
    """ Fixture for a biscuit item example. """
    return {
        "item_id": uuid.uuid4(),
        "codebar": "123456789",
        "name": "Biscuit",
        "description": "Delicious biscuit",
        "price": float(5.0),
        "stock": int(10),
        "state": True,
    }
