# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


from unittest import mock
import pytest
from sqlalchemy.exc import IntegrityError
from src.domain.entities.item import Item
from src.interactor.errors.error_classes import UniqueViolationError

with mock.patch(
    "sqlalchemy.create_engine"
) as mock_create_engine:
    from src.infra.db_models.postgresql.item_db_model import ItemsDBModel
    from .item_postgresql_repository \
        import ItemPostgreSQLRepository


def test_item_postgresql_repository(
        mocker,
        fixture_item_biscuit,
):
    mocker.patch(
        'uuid.uuid4',
        return_value=fixture_item_biscuit['item_id']
    )

    # testing the create method
    items_db_model_mock = mocker.patch(
        'src.infra.repositories.item_postgresql_repository.ItemsDBModel'
    )
    session_mock = mocker.patch(
        'src.infra.repositories.item_postgresql_repository.session'
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
    repository = ItemPostgreSQLRepository()
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

    # testing the create return None
    items_db_model_mock.return_value = None
    result = repository.create(
        fixture_item_biscuit["codebar"],
        fixture_item_biscuit["name"],
        fixture_item_biscuit["description"],
        fixture_item_biscuit["price"],
        fixture_item_biscuit["stock"],
    )
    assert result is None

    # testing sucessful update
    items_edited_db_model = ItemsDBModel(
        item_id=fixture_item_biscuit['item_id'],
        codebar=fixture_item_biscuit['codebar'],
        name="edited_name",
        description=fixture_item_biscuit['description'],
        price=float(20.50),
        stock=int(18),
        state=fixture_item_biscuit['state'],
    )
    items_db_model_mock.return_value = items_edited_db_model
    edited_item = Item(
        items_db_model_mock.return_value.item_id,
        items_db_model_mock.return_value.codebar,
        items_db_model_mock.return_value.name,
        items_db_model_mock.return_value.description,
        items_db_model_mock.return_value.price,
        items_db_model_mock.return_value.stock,
        items_db_model_mock.return_value.state,
    )
    repository = ItemPostgreSQLRepository()
    result = repository.update(
        edited_item
    )
    session_mock.query.assert_called_once_with(items_db_model_mock)
    session_mock.query.return_value.filter_by.return_value.update.\
        assert_called_once_with(
            {
                'codebar': edited_item.codebar,
                'name': edited_item.name,
                'description': edited_item.description,
                'price': edited_item.price,
                'stock': edited_item.stock,
            }
        )
    assert result == edited_item

    # testing update with invalid price
    invalid_item = Item(
        item_id="Dont exist item_id",
        codebar=fixture_item_biscuit['codebar'],
        name="edited_name1",
        description=fixture_item_biscuit['description'],
        price=float(20.50),
        stock=int(18),
        state=fixture_item_biscuit['state'],
    )
    session_mock.query.return_value.filter_by.return_value.update.return_value = 0
    repository = ItemPostgreSQLRepository()
    result_invalid_id = repository.update(
        invalid_item
    )
    assert result_invalid_id is None

    # testing create with name that violates unique constraint
    session_mock.add.side_effect = IntegrityError(
        None,
        None,
        'psycopg2.errors.UniqueViolation: duplicate key value violates unique \
constraint "items_name_key"'
    )
    items_db_model_mock.return_value = None
    with pytest.raises(UniqueViolationError) as exception_info:
        result = repository.create(
            fixture_item_biscuit["codebar"],
            fixture_item_biscuit["name"],
            fixture_item_biscuit["description"],
            fixture_item_biscuit["price"],
            fixture_item_biscuit["stock"],
        )
    assert str(exception_info.value) ==\
        "Item with name: '"+fixture_item_biscuit["name"]+"' already exists"

    # testing create raising another IntegrityError
    session_mock.add.side_effect = IntegrityError(
        None,
        None,
        "test error"
    )
    with pytest.raises(IntegrityError) as exception_info:
        result = repository.create(
            fixture_item_biscuit["codebar"],
            "",
            "",
            fixture_item_biscuit["price"],
            fixture_item_biscuit["stock"],
        )
    assert "test error" in str(exception_info.value)


def test_item_postgresql_repository_get(
        mocker,
        fixture_item_biscuit
):
    session_mock = mocker.patch(
        'src.infra.repositories.item_postgresql_repository.session'
    )
    items_db_model_mock = mocker.patch(
        'src.infra.db_models.postgresql.item_db_model.ItemsDBModel'
    )
    session_mock.query.return_value.get.return_value = \
        items_db_model_mock
    item_mock = Item(
        items_db_model_mock.item_id,
        items_db_model_mock.codebar,
        items_db_model_mock.name,
        items_db_model_mock.description,
        items_db_model_mock.price,
        items_db_model_mock.stock,
        items_db_model_mock.state,
    )
    repository = ItemPostgreSQLRepository()
    result = repository.get(items_db_model_mock.item_id)
    assert result == item_mock

    # testing the case that the query returns None
    session_mock.query.return_value.get.return_value = None
    repository = ItemPostgreSQLRepository()
    result = repository.get(items_db_model_mock.item_id)
    assert result is None
