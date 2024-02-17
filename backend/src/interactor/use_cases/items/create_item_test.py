# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.use_cases.items import create_item
from src.domain.entities.item import Item
from src.interactor.dtos.items.create_item_dtos \
    import CreateItemInputDto, CreateItemOutputDto
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.interfaces.presenters.create_item_presenter \
    import CreateItemPresenterInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotCreatedException


def test_create_item(mocker, fixture_item_biscuit):
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
        CreateItemPresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "create",
    )

    input_dto_validator_mock = mocker.patch(
        "src.interactor.use_cases.items.create_item.\
CreateItemInputDtoValidator",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    repository_mock.create.return_value = item
    presenter_mock.present.return_value = "Test Output"
    use_case = create_item.CreateItemUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = CreateItemInputDto(
        codebar=fixture_item_biscuit['codebar'],
        name=fixture_item_biscuit['name'],
        description=fixture_item_biscuit['description'],
        price=fixture_item_biscuit['price'],
        stock=fixture_item_biscuit['stock'],
        state=fixture_item_biscuit['state'],
    )
    result = use_case.execute(input_dto)
    repository_mock.create.assert_called_once()
    input_dto_validator_mock.assert_called_once_with(input_dto.to_dict())
    input_dto_validator_mock_instance = input_dto_validator_mock.return_value
    input_dto_validator_mock_instance.validate.assert_called_once_with()
    logger_mock.log_info.assert_called_once_with(
        "Item Created Successfully"
    )
    output_dto = CreateItemOutputDto(item)
    presenter_mock.present.assert_called_once_with(output_dto)
    assert result == "Test Output"

    # Test None return value from repository
    repository_mock.create.return_value = None
    item_name = fixture_item_biscuit['name']
    with pytest.raises(ItemNotCreatedException) as excinfo:
        use_case.execute(input_dto)
    assert str(excinfo.value) == f"Item '{item_name}' was not created correctly"


def test_create_item_empty_field(mocker, fixture_item_biscuit):
    presenter_mock = mocker.patch.object(
        CreateItemPresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "create",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    use_case = create_item.CreateItemUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = CreateItemInputDto(
        codebar="",
        name=fixture_item_biscuit['name'],
        description=fixture_item_biscuit['description'],
        price=fixture_item_biscuit['price'],
        stock=fixture_item_biscuit['stock'],
        state=fixture_item_biscuit['state'],
    )
    with pytest.raises(ValueError) as excinfo:
        use_case.execute(input_dto)
    assert str(excinfo.value) == "Codebar: empty values not allowed"
