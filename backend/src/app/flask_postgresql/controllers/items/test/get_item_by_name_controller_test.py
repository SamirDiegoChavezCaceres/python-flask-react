# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from unittest import mock
from src.interactor.dtos.items.get_item_by_name_dtos \
    import GetItemByNameInputDto
from src.interactor.interfaces.logger.logger import LoggerInterface

with mock.patch(
    "sqlalchemy.create_engine"
) as mock_create_engine:
    from src.app.flask_postgresql.controllers.items.\
        get_item_by_name_controller import GetItemByNameController


def test_get_item_by_name_controller(
        monkeypatch,
        mocker,
        fixture_item_biscuit
):
    name = fixture_item_biscuit["name"]
    fake_user_inputs = {
        "name": name,
    }
    monkeypatch.setattr('builtins.input', lambda _: next(fake_user_inputs))

    mock_repository = mocker.patch(
        "src.app.flask_postgresql.controllers.items.\
get_item_by_name_controller.ItemPostgreSQLRepository"
    )
    mocker_presenter = mocker.patch(
        "src.app.flask_postgresql.controllers.items.\
get_item_by_name_controller.GetItemByNamePresenter"
    )
    mock_use_case = mocker.patch(
        "src.app.flask_postgresql.controllers.items.\
get_item_by_name_controller.GetItemByNameUseCase"
    )
    mock_use_case_instance = mock_use_case.return_value
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    result_use_case = {
        "item_id": fixture_item_biscuit["item_id"],
        "codebar": fixture_item_biscuit["codebar"],
        "name": fixture_item_biscuit["name"],
        "description": fixture_item_biscuit["description"],
        "price": fixture_item_biscuit["price"],
        "stock": fixture_item_biscuit["stock"],
        "state": fixture_item_biscuit["state"],
    }
    mock_use_case_instance.execute.return_value = result_use_case

    controller = GetItemByNameController(logger_mock)
    controller.get_item_info(fake_user_inputs)
    result = controller.execute()

    mock_repository.assert_called_once_with()
    mocker_presenter.assert_called_once_with()
    mock_use_case.assert_called_once_with(
        mock_repository.return_value,
        mocker_presenter.return_value,
        logger_mock
    )
    input_dto = GetItemByNameInputDto(
        name=name
    )
    mock_use_case_instance.execute.assert_called_once_with(input_dto)
    assert result["item_id"] == fixture_item_biscuit["item_id"]
    assert result["codebar"] == fixture_item_biscuit["codebar"]
    assert result["name"] == fixture_item_biscuit["name"]
    assert result["description"] == fixture_item_biscuit["description"]
    assert result["price"] == fixture_item_biscuit["price"]
    assert result["stock"] == fixture_item_biscuit["stock"]
    assert result["state"] == fixture_item_biscuit["state"]

    # Test for missing inputs (name)
    fake_user_inputs = {
        "nam": "",
    }
    with pytest.raises(ValueError) as error:
        controller.get_item_info(fake_user_inputs)
    assert str(error.value) == "Missing Item Name"
