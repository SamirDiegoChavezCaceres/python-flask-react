# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from unittest import mock
import pytest
from src.infra.loggers.logger_default import LoggerDefault
from src.interactor.errors.error_classes import UniqueViolationError


with mock.patch(
    "sqlalchemy.create_engine"
) as mock_create_engine:
    from src.app.flask_postgresql.controllers.items.create_item_controller \
        import CreateItemController
    from .create_flask_postgresql_app import create_flask_postgresql_app


logger = LoggerDefault()


@pytest.fixture(name="flask_postgresql_app")
def fixture_flask_postgresql_app():
    """ Fixture for flask app with blueprint
    """
    app = create_flask_postgresql_app(logger)
    app.config.update({
        "TESTING": True,
    })

    yield app


@pytest.fixture(name="client_flask_postgresql_app")
def fixture_client_flask_postgresql_app(flask_postgresql_app):
    """ Fixture to test app_flask_with_blueprint
    """
    return flask_postgresql_app.test_client()


def test_request_item(
        mocker,
        client_flask_postgresql_app,
        fixture_item_biscuit
):
    """ Test request example
    """
    input_data = {
        "codebar": fixture_item_biscuit["codebar"],
        "name": fixture_item_biscuit["name"],
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"]
    }
    item_dict = {
        "item_id": fixture_item_biscuit["item_id"],
        "codebar": fixture_item_biscuit["codebar"],
        "name": fixture_item_biscuit["name"],
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"],
        "state": fixture_item_biscuit["state"]
    }
    controller_mock = mocker.patch(
        "src.app.flask_postgresql.blueprints.items.create_item_blueprint.\
CreateItemController"
    )
    controller_mock.return_value.execute.return_value = item_dict
    response = client_flask_postgresql_app.post(
        "/v1/item/",
        json=input_data
    )
    assert response.status_code == 201
    controller_mock.assert_called_once()
    controller_mock.return_value.get_item_info.assert_called_once_with(
        input_data
    )
    assert b"123456789" in response.data
    assert b"Biscuit" in response.data
    assert b"Delicious biscuit" in response.data
    assert b"5.0" in response.data
    assert b"10" in response.data
    assert b"true" in response.data


def test_request_item_missing_name_error(
        client_flask_postgresql_app,
        fixture_item_biscuit
):
    """ Test request example
    """
    input_data = {
        "codebar": fixture_item_biscuit["codebar"],
        "nam": fixture_item_biscuit["name"],
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/item/",
        json=input_data
    )
    assert b"Missing Item Name" in response.data


def test_request_profession_invalid_name_error(
        client_flask_postgresql_app,
        fixture_item_biscuit
):
    """ Test request invalid name
    """
    input_data = {
        "codebar": fixture_item_biscuit["codebar"],
        "name": "Item",
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/item/",
        json=input_data
    )
    assert b"Name: Item is not permitted" in response.data
    assert response.status_code == 400


def test_request_item_wrong_url_error(
        client_flask_postgresql_app,
        fixture_item_biscuit
):
    """ Test request HTTPException error
    """
    input_data = {
        "codebar": fixture_item_biscuit["codebar"],
        "name": fixture_item_biscuit["name"],
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/ite/",
        json=input_data
    )
    assert b"The requested URL was not found on the server" in response.data
    assert response.status_code == 404


def test_request_profession_unique_error(
        client_flask_postgresql_app,
        fixture_item_biscuit,
        mocker
):
    """ Test handling of unique exception (UniqueViolationError)
    """
    blueprint_mock = mocker.patch.object(
        CreateItemController,
        "execute"
    )
    blueprint_mock.side_effect = UniqueViolationError(
        "item",
        "name",
        fixture_item_biscuit["name"]
    )
    input_data = {
        "codebar": fixture_item_biscuit["codebar"],
        "name": fixture_item_biscuit["name"],
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/item/",
        json=input_data
    )
    assert b"Item with name: 'Biscuit' already exists" in response.data
    assert b'"status_code":409' in response.data
    assert response.status_code == 409


def test_request_profession_500_status_code(
        client_flask_postgresql_app,
        fixture_item_biscuit,
        mocker
):
    """ Test handling of exception that should return a 500 status code
    """
    blueprint_mock = mocker.patch.object(
        CreateItemController,
        "get_item_info"
    )
    blueprint_mock.side_effect = Exception('Unexpected error!')
    input_data = {
        "codebar": fixture_item_biscuit["codebar"],
        "name": fixture_item_biscuit["name"],
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"]
    }
    response = client_flask_postgresql_app.post(
        "/v1/item/",
        json=input_data
    )
    assert b'"status_code":500' in response.data
    assert response.status_code == 500
