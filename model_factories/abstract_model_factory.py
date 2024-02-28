from abc import ABC, abstractmethod
from typing import Any


class AbstractModelFactory(ABC):
    @abstractmethod
    def create_model_instance(self, model_type: str, args: dict) -> Any:
        """
        Creates and returns an object of a specific type.

        Args:
            model_type: Type of model you want to create.
            args: A dictionary containing arguments for object creation.

        Returns:
            An object of a type determined by the concrete factory.
        """
        pass
