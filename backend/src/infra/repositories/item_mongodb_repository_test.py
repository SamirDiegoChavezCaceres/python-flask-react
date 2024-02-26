""" # pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from unittest import mock
import pytest
from pymongo.errors import OperationFailure
from src.domain.entities.item import Item

with mock.patch(
    "pymongo.MongoClient"
) as mock_create_client:
    from src.infra.db_models.mongodb.item_db_model import ItemsDBModel
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
        'src.infra.repositories.item_mongodb_repository.ItemsDBModel'
    )
    collection_mock = mocker.patch(
        'src.infra.repositories.item_mongodb_repository.session'
    )
    items_db_model = ItemsDBModel(
        _id=fixture_item_biscuit['item_id'],
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
        items_db_model_mock.return_value._id,   # pylint: disable=protected-access
        items_db_model_mock.return_value.codebar,
        items_db_model_mock.return_value.name,
        items_db_model_mock.return_value.description,
        items_db_model_mock.return_value.price,
        items_db_model_mock.return_value.stock,
        items_db_model_mock.return_value.state,
    )
    collection_mock.insert_one.assert_called_once_with(
        items_db_model_mock()
    )
    collection_mock.find_one.assert_called_once_with(
        {
            "_id": 
            items_db_model_mock.return_value._id  # pylint: disable=protected-access
        }
    )
    assert result == item

    # testing successful update
    items_edited_db_model = ItemsDBModel(
        _id=fixture_item_biscuit['item_id'],
        codebar=fixture_item_biscuit['codebar'],
        name="Edited Profession name",
        description="Edited Profession description",
        price=fixture_item_biscuit['price'],
        stock=25,
        state=False
    )
    items_db_model_mock.return_value = items_edited_db_model
    edited_item = Item(
        items_db_model_mock.return_value._id,   # pylint: disable=protected-access
        items_db_model_mock.return_value.codebar,
        items_db_model_mock.return_value.name,
        items_db_model_mock.return_value.description,
        items_db_model_mock.return_value.price,
        items_db_model_mock.return_value.stock,
        items_db_model_mock.return_value.state,
    )
    repository = ItemMongoDBRepository()
    result = repository.update(
        edited_item
    )
    collection_mock.update_one.assert_called_once_with(
        {"_id": items_db_model_mock.return_value._id},  # pylint: disable=protected-access
        {"$set": items_db_model_mock.return_value.to_dict()}
    )
    assert result == edited_item

    # testing update with invalid id
    invalid_item = Item(
            item_id="Dont exist item_id",
            codebar=fixture_item_biscuit['codebar'],
            name=fixture_item_biscuit['name'],
            description=fixture_item_biscuit['description'],
            price=fixture_item_biscuit['price'],
            stock=fixture_item_biscuit['stock'],
            state=fixture_item_biscuit['state'],
    )
    collection_mock.update_one.return_value.modified_count = 0
    repository = ItemMongoDBRepository()
    result_invalid_id = repository.update(
        invalid_item
    )
    assert result_invalid_id is None

    # Testing create with name that violate unique
    collection_mock.add.side_effect = OperationFailure(
        None, None,
        'pymongo.errors.OperationFailure: duplicate key value violates unique \
constraint "items_name_key"')
    items_db_model_mock.return_value = None
    with pytest.raises(OperationFailure) as exception_info:
        result = repository.create(
            fixture_item_biscuit["codebar"],
            fixture_item_biscuit["name"],
            fixture_item_biscuit["description"],
            fixture_item_biscuit["price"],
            fixture_item_biscuit["stock"],
        )
    assert str(exception_info.value) == \
        "Item with name: '"+fixture_item_biscuit["name"]+"' already exists"

    # Testing create raising another IntegrityError
    collection_mock.add.side_effect = OperationFailure(None, None, "test error")
    with pytest.raises(OperationFailure) as exception_info:
        result = repository.create(
            fixture_item_biscuit["codebar"],
            fixture_item_biscuit["name"],
            fixture_item_biscuit["description"],
            fixture_item_biscuit["price"],
            fixture_item_biscuit["stock"],
        )
    assert "test error" in str(exception_info.value)


def test_item_mongodb_repository_get(
        mocker,
        fixture_item_biscuit,
):

    collection_mock = mocker.patch(
        #'src.infra.db_models.mongodb.mongodb_base.session.items'
        'src.infra.repositories.item_mongodb_repository.session.items'
    )
    items_db_model_mock = mocker.patch(
        'src.infra.db_models.mongodb.item_db_model.ItemsDBModel'
    )
    collection_mock.find_one.return_value = \
        items_db_model_mock
    item_mock = Item(
        items_db_model_mock._id,
        items_db_model_mock.codebar,
        items_db_model_mock.name,
        items_db_model_mock.description,
        items_db_model_mock.price,
        items_db_model_mock.stock,
        items_db_model_mock.state,
    )
    #items_db_model_mock.return_value = items_db_model
    repository = ItemMongoDBRepository()
    result = repository.get(
        items_db_model_mock._id   # pylint: disable=protected-access
    )
    assert result == item_mock

    # Testing the case that the query returns None
    collection_mock.query.return_value.get.return_value = None
    repository = ItemMongoDBRepository()
    result = repository.get(
        items_db_model_mock._id  # pylint: disable=protected-access
    )
    assert result is None
 """