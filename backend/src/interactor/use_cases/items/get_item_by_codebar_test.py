# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.use_cases.items.get_item_by_codebar \
    import GetItemByCodebarUseCase
from src.domain.entities.item import Item
from src.interactor.dtos.items.get_by_codebar_dtos \
    import GetItemByCodebarInputDto, GetItemByCodebarOutputDto
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.interfaces.presenters.items.get_by_codebar_presenter \
    import GetItemByCodebarPresenterInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException


def test_get_item_by_codebar(mocker, fixture_item_biscuit):
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
        GetItemByCodebarPresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "get_by_codebar",
    )

    input_dto_validator_mock = mocker.patch(
        "src.interactor.use_cases.items.get_item_by_codebar.\
GetItemByCodebarInputDtoValidator",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    repository_mock.get_by_codebar.return_value = item
    presenter_mock.present.return_value = "Test Output"
    use_case = GetItemByCodebarUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = GetItemByCodebarInputDto(
        codebar=fixture_item_biscuit['codebar']
    )
    result = use_case.execute(input_dto)
    repository_mock.get_by_codebar.assert_called_once()
    input_dto_validator_mock.assert_called_once_with(input_dto.to_dict())
    input_dto_validator_mock_instance = input_dto_validator_mock.return_value
    input_dto_validator_mock_instance.validate.assert_called_once_with()
    logger_mock.log_info.assert_called_once_with(
        "Item Retrieved Successfully"
    )
    output_dto = GetItemByCodebarOutputDto(item)
    presenter_mock.present.assert_called_once_with(output_dto)
    assert result == "Test Output"

    # Test None Return from repository
    repository_mock.get_by_codebar.return_value = None
    codebar =  fixture_item_biscuit['codebar']
    with pytest.raises(ItemNotFoundException) as exc_info:
        use_case.execute(input_dto)
    assert str(exc_info.value) == f"Item with codebar: {codebar} not found"


def test_get_item_by_codebar_with_empty_field(mocker):
    presenter_mock = mocker.patch.object(
        GetItemByCodebarPresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "get_by_codebar",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    input_dto = GetItemByCodebarInputDto(
        codebar=""
    )
    use_case = GetItemByCodebarUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    with pytest.raises(ValueError) as excinfo:
        use_case.execute(input_dto)
    assert str(excinfo.value) == "Codebar: empty values not allowed"
