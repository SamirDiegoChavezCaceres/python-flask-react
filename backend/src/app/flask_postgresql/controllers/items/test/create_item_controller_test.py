# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import pytest
from unittest import mock
from src.interactor.dtos.items.create_item_dtos import CreateItemInputDto
from src.interactor.interfaces.logger.logger import LoggerInterface

with mock.patch(
    "sqlalchemy.create_engine"
) as mock_create_engine:
    from src.app.flask_postgresql.controllers.items.create_item_controller \
        import CreateItemController


def test_create_item_controller(monkeypatch, mocker, fixture_item_biscuit):
    name = fixture_item_biscuit["name"]
    codebar = fixture_item_biscuit["codebar"]
    description = fixture_item_biscuit["description"]
    price = fixture_item_biscuit["price"]
    stock = fixture_item_biscuit["stock"]
    fake_user_inputs = {
        "name": name,
        "codebar": codebar,
        "description": description,
        "price": price,
        "stock": stock
    }
    monkeypatch.setattr('builtins.input', lambda _: next(fake_user_inputs))

    mock_repository = mocker.patch(
        "src.app.flask_postgresql.controllers.items.create_item_controller.\
ItemPostgreSQLRepository"
    )
    mocker_presenter = mocker.patch(
        "src.app.flask_postgresql.controllers.items.create_item_controller.\
CreateItemPresenter"
    )
    mock_use_case = mocker.patch(
        "src.app.flask_postgresql.controllers.items.create_item_controller.\
CreateItemUseCase"
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

    controller = CreateItemController(logger_mock)
    controller.get_item_info(fake_user_inputs)
    result = controller.execute()

    mock_repository.assert_called_once_with()
    mocker_presenter.assert_called_once_with()
    mock_use_case.assert_called_once_with(
        mock_repository.return_value,
        mocker_presenter.return_value,
        logger_mock
    )
    input_dto = CreateItemInputDto(
        name=name,
        codebar=codebar,
        description=description,
        price=price,
        stock=stock
    )
    mock_use_case_instance.execute.assert_called_once_with(input_dto)
    assert result["codebar"] == fixture_item_biscuit["codebar"]
    assert result["name"] == fixture_item_biscuit["name"]
    assert result["description"] == fixture_item_biscuit["description"]
    assert result["price"] == fixture_item_biscuit["price"]
    assert result["stock"] == fixture_item_biscuit["stock"]

    # Test for missing inputs (name)
    fake_user_inputs = {
        "nam": name,
        "codebar": codebar,
        "description": description,
        "price": price,
        "stock": stock
    }
    with pytest.raises(ValueError) as excinfo:
        controller.get_item_info(fake_user_inputs)
    assert str(excinfo.value) == "Missing Item Name"

    # Test for missing inputs (codebar)
    fake_user_inputs = {
        "name": name,
        "codeba": codebar,
        "description": description,
        "price": price,
        "stock": stock
    }
    with pytest.raises(ValueError) as excinfo:
        controller.get_item_info(fake_user_inputs)
    assert str(excinfo.value) == "Missing Item Codebar"

    # Test for missing inputs (description)
    fake_user_inputs = {
        "name": name,
        "codebar": codebar,
        "descriptio": description,
        "price": price,
        "stock": stock
    }
    with pytest.raises(ValueError) as excinfo:
        controller.get_item_info(fake_user_inputs)
    assert str(excinfo.value) == "Missing Item Description"

    # Test for missing inputs (price)
    fake_user_inputs = {
        "name": name,
        "codebar": codebar,
        "description": description,
        "pric": price,
        "stock": stock
    }
    with pytest.raises(ValueError) as excinfo:
        controller.get_item_info(fake_user_inputs)
    assert str(excinfo.value) == "Missing Item Price"

    # Test for missing inputs (stock)
    fake_user_inputs = {
        "name": name,
        "codebar": codebar,
        "description": description,
        "price": price,
        "stoc": stock
    }
    with pytest.raises(ValueError) as excinfo:
        controller.get_item_info(fake_user_inputs)
    assert str(excinfo.value) == "Missing Item Stock"

        