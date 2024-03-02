""" This module contains exceptions for the Use Cases layer.
"""


class FieldValueNotPermittedException(Exception):
    """ This exception is raised when a field value is not permitted.
    """
    def __init__(self, field_name: str, field_value: str) -> None:
        self.field_name = field_name
        self.field_value = field_value

    def __str__(self) -> str:
        return f"{self.field_name.capitalize()}: {self.field_value} is not \
permitted"


class ItemNotCreatedException(Exception):
    """ This exception is raised when an item is not created.
    """
    def __init__(self, item_name: str, item_type: str) -> None:
        self.item_name = item_name
        self.item_type = item_type

    def __str__(self) -> str:
        return f"{self.item_type.capitalize()} '{self.item_name}' was not \
created correctly"


class UniqueViolationError(Exception):
    """ This exception is raised when a unique constraint is violated.
    """
    def __init__(self,
                    table_name: str,
                    field_name: str,
                    field_value: str
    ) -> None:
        self.table_name = table_name
        self.field_name = field_name
        self.field_value = field_value


    def __str__(self) -> str:
        return f"{self.table_name.capitalize()} with {self.field_name}: \
'{self.field_value}' already exists"


class ItemNotFoundException(Exception):
    """ This exception is raised when an item is not found.
    """
    def __init__(self, field_name, item_id: str) -> None:
        self.field_name = field_name
        self.item_id = item_id

    def __str__(self) -> str:
        return f"Item with {self.field_name}: {self.item_id} not found"


class ItemsNotFoundException(Exception):
    """ This exception is raised when items are not found.
    """
    def __str__(self) -> str:
        return "Items not found"
