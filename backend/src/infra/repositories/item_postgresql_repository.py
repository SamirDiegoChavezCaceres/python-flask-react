""" Module for ItemPostgreSQLRepository
"""


from typing import Optional
import uuid
from sqlalchemy.exc import IntegrityError
from src.domain.entities.item import Item
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.domain.value_objects import ItemId
from src.infra.db_models.postgresql.postgresql_base import session
from src.infra.db_models.postgresql.item_db_model import ItemsDBModel
from src.interactor.errors.error_classes import UniqueViolationError


class ItemPostgreSQLRepository(ItemRepositoryInterface):
    """ PostgreSQL repository for Item
    """
    def __init__(self) -> None:
        self.__session = session

    def __db_to_entity(
            self,
            db_row: ItemsDBModel
    ) -> Optional[Item]:
        return Item(
            item_id = db_row.item_id,
            codebar = db_row.codebar,
            name = db_row.name,
            description = db_row.description,
            price = db_row.price,
            stock = db_row.stock,
            state = db_row.state,
        )

    def get(self, item_id: ItemId) -> Optional[Item]:
        """ Get an item by id
        :param item_id: ItemId
        :return: Optional[Item]
        """
        result = self.__session.query(
            ItemsDBModel
        ).get(
           item_id
        )
        if result is not None:
            return self.__db_to_entity(result)
        return None

    def create(
            self,
            codebar: str,
            name: str,
            description: str,
            price: float,
            stock: int
    ) -> Optional[Item]:
        """ Create a new item
        :param name: str
        :param codebar: str
        :param description: str
        :param price: float
        :param stock: int
        :return: Optional[Item]
        """
        item_id = uuid.uuid4()
        item_db_model = ItemsDBModel(
            item_id=item_id,
            codebar=codebar,
            name=name,
            description=description,
            price=price,
            stock=stock,
            state=True,
        )

        try:
            self.__session.add(item_db_model)
            self.__session.commit()
            self.__session.refresh(item_db_model)
        except IntegrityError as error:
            if "violates unique constraint" in str(error):
                raise UniqueViolationError(
                    "Item", "name", name
                ) from error
            raise

        if item_db_model is not None:
            return self.__db_to_entity(item_db_model)
        return None


    def update(self, item: Item) -> Optional[Item]:
        """ Update an item
        :param item: Item
        :return: Optional[Item]
        """
        item_db_model = ItemsDBModel(
            item_id=item.item_id,
            codebar=item.codebar,
            name=item.name,
            description=item.description,
            price=item.price,
            stock=item.stock,
            state=item.state,
        )
        result = self.__session.query(
            ItemsDBModel
        ).filter_by(
            item_id=item.item_id
        ).update(
            {
                'codebar': item.codebar,
                'name': item.name,
                'description': item.description,
                'price': item.price,
                'stock': item.stock,
            }
        )
        if result == 0:
            return None
        self.__session.commit()
        return self.__db_to_entity(item_db_model)

    def delete(self, item_id: ItemId) -> Optional[Item]:
        """ Delete an item
        :param item_id: ItemId
        :return: Optional[Item]
        """
        item_db_model = self.__session.query(
            ItemsDBModel
        ).filter_by(
            item_id=item_id
        ).first()
        if item_db_model is not None:
            self.__session.delete(item_db_model)
            self.__session.commit()
            return self.__db_to_entity(item_db_model)
        return None

    def get_all(self) -> list[Item]:
        """ Get all items
        :return: list[Item]
        """
        items = []
        for item in self.__session.query(ItemsDBModel).all():
            items.append(self.__db_to_entity(item))
        return items

    def get_by_codebar(self, codebar: str) -> Optional[Item]:
        """ Get an item by codebar
        :param codebar: str
        :return: Optional[Item]
        """
        item_db_model = self.__session.query(
            ItemsDBModel
        ).filter_by(
            codebar=codebar
        ).first()
        if item_db_model is not None:
            return self.__db_to_entity(item_db_model)
        return None

    def get_by_name(self, name: str) -> Optional[Item]:
        """ Get an item by name
        :param name: str
        :return: Optional[Item]
        """
        item_db_model = self.__session.query(
            ItemsDBModel
        ).filter_by(
            name=name
        ).first()
        if item_db_model is not None:
            return self.__db_to_entity(item_db_model)
        return None

    def activate(self, item_id: ItemId) -> Optional[Item]:
        """ Activate an item
        :param item_id: ItemId
        :return: Optional[Item]
        """
        item = self.get(item_id)
        if item is not None:
            result = self.__session.query(
                ItemsDBModel
            ).filter_by(
                item_id=item_id
            ).update(
                {
                    'state': True
                }
            )
            self.__session.commit()
            if result == 0:
                return None
            return item
        return None

    def deactivate(self, item_id: ItemId) -> Optional[Item]:
        """ Deactivate an item
        :param item_id: ItemId
        :return: Optional[Item]
        """
        item = self.get(item_id)
        if item is not None:
            result = self.__session.query(
                ItemsDBModel
            ).filter_by(
                item_id=item_id
            ).update(
                {
                    'state': False
                }
            )
            self.__session.commit()
            if result == 0:
                return None
            return item
        return None
