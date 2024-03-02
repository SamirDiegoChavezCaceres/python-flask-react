# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring


import pytest
from src.interactor.use_cases.items import get_all_items
from src.domain.entities.item import Item
from src.interactor.dtos.items.get_all_items_dtos \
    import GetAllItemsOutputDto
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.interactor.interfaces.presenters.items.get_all_items_presenter \
    import GetAllItemsPresenterInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from src.interactor.errors.error_classes import ItemsNotFoundException


def test_get_all_items(mocker, fixture_item_biscuit, fixture_item_chocolate):
    items = [
        Item(
            item_id=fixture_item_biscuit['item_id'],
            codebar=fixture_item_biscuit['codebar'],
            name=fixture_item_biscuit['name'],
            description=fixture_item_biscuit['description'],
            price=fixture_item_biscuit['price'],
            stock=fixture_item_biscuit['stock'],
            state=fixture_item_biscuit['state'],
        ),
        Item(
            item_id=fixture_item_chocolate['item_id'],
            codebar=fixture_item_chocolate['codebar'],
            name=fixture_item_chocolate['name'],
            description=fixture_item_chocolate['description'],
            price=fixture_item_chocolate['price'],
            stock=fixture_item_chocolate['stock'],
            state=fixture_item_chocolate['state'],
        ),
    ]
    presenter_mock = mocker.patch.object(
        GetAllItemsPresenterInterface,
        "present",
    )
    repository_mock = mocker.patch.object(
        ItemRepositoryInterface,
        "get_all",
    )

    logger_mock = mocker.patch.object(LoggerInterface, "log_info")
    repository_mock.get_all.return_value = items
    presenter_mock.present.return_value = "Test Output"
    use_case = get_all_items.GetAllItemsUseCase(
        presenter_mock,
        repository_mock,
        logger_mock
    )
    result = use_case.execute()
    repository_mock.get_all.assert_called_once()
    logger_mock.log_info.assert_called_once_with(
        "Items Retrieved Successfully"
    )
    output_dto = GetAllItemsOutputDto(items)
    presenter_mock.present.assert_called_once_with(output_dto)
    assert result == "Test Output"

    # Test None return from repository
    repository_mock.get_all.return_value = None
    with pytest.raises(ItemsNotFoundException) as exc_info:
        use_case.execute()
    assert str(exc_info.value) == "Items not found"
