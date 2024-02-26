""" Module for ItemMongoDBRepository
"""


from typing import Optional
import uuid
from src.domain.entities.item import Item
from src.interactor.interfaces.repositories.item_repository \
    import ItemRepositoryInterface
from src.domain.value_objects import ItemId
from src.infra.db_models.mongodb.mongodb_base import session
from src.infra.db_models.mongodb.item_db_model import ItemsDBModel
from src.interactor.errors.error_classes import UniqueViolationError


class ItemMongoDBRepository(ItemRepositoryInterface):
    """ MongoDB repository for Item
    """
    def __init__(self) -> None:
        self.__collection = session["items"]

    def __db_to_entity(self, db_row: ItemsDBModel) -> Optional[Item]:
        return Item(
            db_row._id, # pylint: disable=protected-access
            db_row.codebar,
            db_row.name,
            db_row.description,
            db_row.price,
            db_row.stock,
            db_row.state,
        )

    def create(
            self,
            codebar: str,
            name: str,
            description: str,
            price: float,
            stock: int
    ) -> Optional[Item]:
        """ Create a new item
        :param codebar: str
        :param name: str
        :param description: str
        :param price: float
        :param stock: int
        :param state: bool
        :return: Optional[Item]
        """
        item_id = str(uuid.uuid4())
        item_db_model = ItemsDBModel(
            _id=item_id,
            codebar=codebar,
            name=name,
            description=description,
            price=price,
            stock=stock,
        )

        __collection = self.__collection
        if __collection.find_one({"codebar": item_db_model.codebar}) is not None:
            raise UniqueViolationError(
                "Item", "codebar", codebar
            )
        else:
            __collection.insert_one(item_db_model.to_dict())
            item_db_model =\
                __collection.find_one(
                    {
                        "_id": 
                        item_db_model._id # pylint: disable=protected-access
                    }
                )

        if item_db_model is not None:
            return self.__db_to_entity(item_db_model)
        return None

    def get(self, item_id: ItemId) -> Optional[Item]:
        """ Get an item
        :param item_id: ItemId
        :return: Optional[Item]
        """
        item_db_model = self.__collection.find_one({"_id": item_id})
        if item_db_model is not None:
            return self.__db_to_entity(item_db_model)
        return None

    def update(self, item: Item) -> Optional[Item]:
        """ Update an item
        :param item: Item
        :return: Optional[Item]
        """
        item_db_model = ItemsDBModel(
            _id=item._id,  # pylint: disable=protected-access
            codebar=item.codebar,
            name=item.name,
            description=item.description,
            price=item.price,
            stock=item.stock,
        )
        result = self.__collection.update_one(
            {"_id": item._id},  # pylint: disable=protected-access
            {"$set": item_db_model.to_dict()}
        )
        if result.modified_count == 0:
            return None
        return self.__db_to_entity(item_db_model)

    def delete(self, item_id: ItemId) -> Optional[Item]:
        """ Delete an item
        :param item_id: ItemId
        :return: Optional[Item]
        """
        item = self.get(item_id)
        if item is not None:
            result = self.__collection.delete_one({"_id": item_id})
        if result.deleted_count == 0:
            return None
        return item

    def get_all(self) -> list[Item]:
        """ Get all items
        :return: list[Item]
        """
        items = []
        for item in self.__collection.find():
            items.append(self.__db_to_entity(item))
        return items

    def get_by_codebar(self, codebar: str) -> Optional[Item]:
        """ Get an item by codebar
        :param codebar: str
        :return: Optional[Item]
        """
        item_db_model = self.__collection.find_one({"codebar": codebar})
        if item_db_model is not None:
            return self.__db_to_entity(item_db_model)
        return None

    def get_by_name(self, name: str) -> Optional[Item]:
        """ Get an item by name
        :param name: str
        :return: Optional[Item]
        """
        item_db_model = self.__collection.find_one({"name": name})
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
            result = self.__collection.update_one(
                {"_id": item_id},
                {"$set": {"state": True}}
            )
        if result.modified_count == 0:
            return None
        return item

    def deactivate(self, item_id: ItemId) -> Optional[Item]:
        """ Deactivate an item
        :param item_id: ItemId
        :return: Optional[Item]
        """
        item = self.get(item_id)
        if item is not None:
            result = self.__collection.update_one(
                {"_id": item_id},
                {"$set": {"state": False}}
            )
        if result.modified_count == 0:
            return None
        return item
