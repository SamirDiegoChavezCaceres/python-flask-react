# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.use_cases.items.get_item_by_name \
    import GetItemByNameUseCase
from src.domain.entities.item import Item
from src.interactor.dtos.items.get_item_by_name_dtos \
    import GetItemByNameInputDto, GetItemByNameOutputDto
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.interfaces.presenters.items.get_item_by_name_presenter \
    import GetItemByNamePresenterInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException


def test_get_item(mocker, fixture_item_biscuit):
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
        GetItemByNamePresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "get_by_name",
    )

    input_dto_validator_mock = mocker.patch(
        "src.interactor.use_cases.items.get_item_by_name.\
GetItemByNameInputDtoValidator",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    repository_mock.get_by_name.return_value = item
    presenter_mock.present.return_value = "Test Output"
    use_case = GetItemByNameUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = GetItemByNameInputDto(
        name=fixture_item_biscuit['name']
    )
    result = use_case.execute(input_dto)
    repository_mock.get_by_name.assert_called_once()
    input_dto_validator_mock.assert_called_once_with(input_dto.to_dict())
    input_dto_validator_mock_instance = input_dto_validator_mock.return_value
    input_dto_validator_mock_instance.validate.assert_called_once_with()
    logger_mock.log_info.assert_called_once_with(
        "Item Retrieved Successfully"
    )
    output_dto = GetItemByNameOutputDto(item)
    presenter_mock.present.assert_called_once_with(output_dto)
    assert result == "Test Output"

    # Test None return from repository
    repository_mock.get_by_name.return_value = None
    name = fixture_item_biscuit['name']
    with pytest.raises(ItemNotFoundException) as exc_info:
        use_case.execute(input_dto)
    assert str(exc_info.value) == f"Item with name: {name} not found"


def test_get_item_by_name_with_empty_field(mocker):
    presenter_mock = mocker.patch.object(
        GetItemByNamePresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "get_by_name",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_exception")
    input_dto = GetItemByNameInputDto(
        name=""
    )
    use_case = GetItemByNameUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    with pytest.raises(ValueError) as excinfo:
        use_case.execute(input_dto)
    assert str(excinfo.value) == "Name: empty values not allowed"
