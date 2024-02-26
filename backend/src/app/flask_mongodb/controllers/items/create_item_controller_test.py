""" # pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from unittest import mock
from src.interactor.dtos.items.create_item_dtos import CreateItemInputDto
from src.interactor.interfaces.logger.logger import LoggerInterface


with mock.patch(
    "pymongo.MongoClient"
) as mock_create_client:
    from src.app.flask_mongodb.controllers.items.create_item_controller \
        import CreateItemController
    

def test_create_item(monkeypatch, mocker, fixture_item_biscuit):
    codebar = fixture_item_biscuit['codebar']
    name = fixture_item_biscuit['name']
    description = fixture_item_biscuit['description']
    price = fixture_item_biscuit['price']
    stock = fixture_item_biscuit['stock']
    state = fixture_item_biscuit['state']
    fake_user_inputs = {
        "codebar": codebar,
        "name": name,
        "description": description,
        "price": price,
        "stock": stock,
        "state": state,
    }
    monkeypatch.setattr('builtins.input', lambda _: next(fake_user_inputs))

    mock_repository = mocker.patch(
        'src.app.flask_mongodb.controllers.items.create_item_controller.\
ItemMongoDBRepository'
    )
    mock_presenter = mocker.patch(
        'src.app.flask_mongodb.controllers.items.create_item_controller.\
CreateItemPresenter'
    )
    mock_use_case = mocker.patch(
        'src.app.flask_mongodb.controllers.items.create_item_controller.\
CreateItemUseCase'
    )
    mock_use_case_instance = mock_use_case.return_value
    logger_mock = mocker.patch.object(LoggerInterface, 'log_info')
    result_use_case = {
        "item_id": fixture_item_biscuit['item_id'],
        "codebar": codebar,
        "name": name,
        "description": description,
        "price": price,
        "stock": stock,
        "state": state,
    }
    mock_use_case_instance.execute.return_value = result_use_case

    controller = CreateItemController(logger_mock)
    controller.get_item_info(fake_user_inputs)
    result = controller.execute()

    mock_repository.assert_called_once_with()
    mock_presenter.assert_called_once_with()
    mock_use_case.assert_called_once_with(
        mock_presenter.return_value,
        mock_repository.return_value,
        logger_mock
    )
    input_dto = CreateItemInputDto(
        codebar=codebar,
        name=name,
        description=description,
        price=price,
        stock=stock,
        state=state
    )
    mock_use_case_instance.execute.assert_called_once_with(input_dto)
    assert result["codebar"] == codebar
    assert result["name"] == name
    assert result["description"] == description
    assert result["price"] == price
    assert result["stock"] == stock
    assert result["state"] == state
 """