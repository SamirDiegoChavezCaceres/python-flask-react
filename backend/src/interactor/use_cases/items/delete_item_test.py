# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.use_cases.items.delete_item \
    import DeleteItemUseCase
from src.domain.entities.item import Item
from src.interactor.dtos.items.delete_item_dtos \
    import DeleteItemInputDto, DeleteItemOutputDto
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.interfaces.presenters.items.delete_item_presenter \
    import DeleteItemPresenterInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemNotFoundException


def test_delete_item(mocker, fixture_item_biscuit):
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
        DeleteItemPresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "delete",
    )

    input_dto_validator_mock = mocker.patch(
        "src.interactor.use_cases.items.delete_item.\
DeleteItemInputDtoValidator",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    repository_mock.delete.return_value = item
    presenter_mock.present.return_value = "Test Output"
    use_case = DeleteItemUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = DeleteItemInputDto(
        item_id=fixture_item_biscuit['item_id']
    )
    result = use_case.execute(input_dto)
    repository_mock.delete.assert_called_once()
    input_dto_validator_mock.assert_called_once_with(input_dto.to_dict())
    input_dto_validator_mock_instance = input_dto_validator_mock.return_value
    input_dto_validator_mock_instance.validate.assert_called_once_with()
    logger_mock.log_info.assert_called_once_with(
        "Item Deleted Successfully"
    )
    output_dto = DeleteItemOutputDto(item)
    presenter_mock.present.assert_called_once_with(output_dto)
    assert result == "Test Output"

    # Test ItemNotFoundException
    repository_mock.delete.return_value = None
    item_id = fixture_item_biscuit['item_id']
    with pytest.raises(ItemNotFoundException) as exc:
        use_case.execute(input_dto)
    assert str(exc.value) == f"Item with id: {item_id} not found"


def test_delete_item_with_empty_field(mocker):
    presenter_mock = mocker.patch.object(
        DeleteItemPresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "delete",
    )
    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    use_case = DeleteItemUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    input_dto = DeleteItemInputDto(
        item_id=""
    )
    with pytest.raises(ValueError) as exc:
        use_case.execute(input_dto)
    assert str(exc.value) == "Item_id: empty values not allowed"
