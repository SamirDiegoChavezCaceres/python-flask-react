# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.use_cases.items import update_item
from src.domain.entities.item import Item
from src.interactor.dtos.items.update_item_dtos \
    import UpdateItemInputDto, UpdateItemOutputDto
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.interfaces.presenters.items.update_item_presenter \
    import UpdateItemPresenterInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException


def test_update_item(mocker, fixture_item_biscuit):
    item = Item(
        item_id=fixture_item_biscuit['item_id'],
        codebar=fixture_item_biscuit['codebar'],
        name=fixture_item_biscuit['name'],
        description=fixture_item_biscuit['description'],
        price=fixture_item_biscuit['price'],
        stock=fixture_item_biscuit['stock'],
        state=fixture_item_biscuit['state'],
    )
    presenter_mock = mocker.patch.object(
        UpdateItemPresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "update",
    )

    input_dto_validator_mock = mocker.patch(
        "src.interactor.use_cases.items.update_item.\
UpdateItemInputDtoValidator",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    repository_mock.update.return_value = item
    presenter_mock.present.return_value = "Test Output"
    use_case = update_item.UpdateItemUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = UpdateItemInputDto(
        item_id=fixture_item_biscuit['item_id'],
        codebar=fixture_item_biscuit['codebar'],
        name=fixture_item_biscuit['name'],
        description=fixture_item_biscuit['description'],
        price=fixture_item_biscuit['price'],
        stock=fixture_item_biscuit['stock'],
        state=fixture_item_biscuit['state'],
    )
    result = use_case.execute(input_dto)
    repository_mock.update.assert_called_once()
    input_dto_validator_mock_instance = input_dto_validator_mock.return_value
    input_dto_validator_mock_instance.validate.assert_called_once_with()
    logger_mock.log_info.assert_called_once_with(
        "Item Saved Successfully"
    )
    output_dto = UpdateItemOutputDto(item)
    presenter_mock.present.assert_called_once_with(output_dto)
    assert result == "Test Output"

    # Test None return value from repository
    repository_mock.update.return_value = None
    item_id = fixture_item_biscuit['item_id']
    with pytest.raises(ItemNotFoundException) as exc_info:
        use_case.execute(input_dto)
    assert str(exc_info.value) == f"Item with id: {item_id} not found"


def test_update_item_empty_field(mocker, fixture_item_biscuit):
    presenter_mock = mocker.patch.object(
        UpdateItemPresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "update",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    use_case = update_item.UpdateItemUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = UpdateItemInputDto(
        item_id=fixture_item_biscuit['item_id'],
        codebar=fixture_item_biscuit['codebar'],
        name="",
        description=fixture_item_biscuit['description'],
        price=fixture_item_biscuit['price'],
        stock=fixture_item_biscuit['stock'],
        state=fixture_item_biscuit['state'],
    )
    with pytest.raises(ValueError) as excinfo:
        use_case.execute(input_dto)
    assert str(excinfo.value) == "Name: empty values not allowed"
