# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest


@pytest.fixture
def fixture_item_biscuit():
    """ Fixture for a biscuit item example. """
    return {
        "item_id": "1",
        "codebar": "123456789",
        "name": "Biscuit",
        "description": "Delicious biscuit",
        "price": 5.0,
        "stock": 10,
        "state": "active",
    }
