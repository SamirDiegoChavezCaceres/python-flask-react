# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from unittest import mock
from src.interactor.interfaces.logger.logger import LoggerInterface

with mock.patch(
    "sqlalchemy.create_engine"
) as mock_create_engine:
    from src.app.flask_postgresql.controllers.items.get_all_items_controller \
        import GetAllItemsController


def test_get_all_items_controller(monkeypatch, mocker, fixture_item_biscuit):
    fake_user_inputs = {}
    monkeypatch.setattr('builtins.input', lambda _: next(fake_user_inputs))

    mock_repository = mocker.patch(
        "src.app.flask_postgresql.controllers.items.get_all_items_controller.\
ItemPostgreSQLRepository"
    )
    mocker_presenter = mocker.patch(
        "src.app.flask_postgresql.controllers.items.get_all_items_controller.\
GetAllItemsPresenter"
    )
    mock_use_case = mocker.patch(
        "src.app.flask_postgresql.controllers.items.get_all_items_controller.\
GetAllItemsUseCase"
    )
    mock_use_case_instance = mock_use_case.return_value
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    result_use_case = {
        "items": [
            {
                "item_id": fixture_item_biscuit["item_id"],
                "codebar": fixture_item_biscuit["codebar"],
                "name": fixture_item_biscuit["name"],
                "description": fixture_item_biscuit["description"],
                "price": fixture_item_biscuit["price"],
                "stock": fixture_item_biscuit["stock"],
                "state": fixture_item_biscuit["state"],
            }
        ]
    }
    mock_use_case_instance.execute.return_value = result_use_case

    controller = GetAllItemsController(logger_mock)
    result = controller.execute()

    mock_repository.assert_called_once_with()
    mocker_presenter.assert_called_once_with()
    mock_use_case.assert_called_once_with(
        mock_repository.return_value,
        mocker_presenter.return_value,
        logger_mock
    )
    mock_use_case_instance.execute.assert_called_once_with()
    assert result["items"] == result_use_case["items"]
    assert result["items"][0]["item_id"] == fixture_item_biscuit["item_id"]
    assert result["items"][0]["codebar"] == fixture_item_biscuit["codebar"]
    assert result["items"][0]["name"] == fixture_item_biscuit["name"]
    assert result["items"][0]["description"] == fixture_item_biscuit["description"]
    assert result["items"][0]["price"] == fixture_item_biscuit["price"]
    assert result["items"][0]["stock"] == fixture_item_biscuit["stock"]
    assert result["items"][0]["state"] == fixture_item_biscuit["state"]
