""" Defines the validator for the get item input data.
"""


from typing import Dict
from src.interactor.validations.base_input_validator import BaseInputValidator


class GetItemByNameInputDtoValidator(BaseInputValidator):
    """ Validates the get item input data.
    :param input_data: The input data to be validated.
    """

    def __init__(self, input_data: Dict) -> None:
        super().__init__(input_data)
        self.input_data = input_data
        self.__schema = {
            "name": {
                "empty": False,
                "required": True,
            }
        }

    def validate(self) -> None:
        """ Validates the input data
        """
        # Verify the input data using BaseInputValidator method
        super().verify(self.__schema)
