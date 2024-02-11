# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from unittest import mock
import pytest 
from pymongo.errors import OperationFailure
from src.domain.entities.item import Item
from src.interactor.errors.error_classes import UniqueViolationError

with mock.patch(
    "pymongo.MongoClient"
) as mock_create_client:
    from src.infra.db_models.item_db_model import ItemsDBModel
    from .item_mongodb_repository import ItemMongoDBRepository

def test_item_mongodb_repository(
        mocker,
        fixture_item_biscuit,
):
    
    mocker.patch(
        'uuid.uuid4',
        return_value=fixture_item_biscuit['item_id']
    )

    # testing the create method
    items_db_model_mock = mocker.patch(
        'src.infra.repositories.profession_mongodb_repository.ItemDBModel'
    )
    session_mock = mocker.patch(
        'src.infra.repositories.profession_mongodb_repository.Session'
    )
    items_db_model = ItemsDBModel(
        item_id=fixture_item_biscuit['item_id'],
        codebar=fixture_item_biscuit['codebar'],
        name=fixture_item_biscuit['name'],
        description=fixture_item_biscuit['description'],
        price=fixture_item_biscuit['price'],
        stock=fixture_item_biscuit['stock'],
        state=fixture_item_biscuit['state'],
    )
    items_db_model_mock.return_value = items_db_model
    repository = ItemMongoDBRepository()
    result = repository.create(
        fixture_item_biscuit["codebar"],
        fixture_item_biscuit["name"],
        fixture_item_biscuit["description"],
        fixture_item_biscuit["price"],
        fixture_item_biscuit["stock"],
    )
    item = Item(
        items_db_model_mock.return_value.item_id,
        items_db_model_mock.return_value.codebar,
        items_db_model_mock.return_value.name,
        items_db_model_mock.return_value.description,
        items_db_model_mock.return_value.price,
        items_db_model_mock.return_value.stock,
        items_db_model_mock.return_value.state,
    )
    session_mock.add.assert_called_once_with(items_db_model_mock())
    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(items_db_model_mock())
    assert result == item
    