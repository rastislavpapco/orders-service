import inspect

import database.database
from database.database import Base
from .abstract_model_factory import AbstractModelFactory


class DatabaseModelFactory(AbstractModelFactory):
    DATABASE_CLASSES_MAPPING = {name: cls for name, cls in inspect.getmembers(database.database, inspect.isclass)
                                if issubclass(cls, Base)}

    @classmethod
    def create_model_instance(cls, model_type: str, args: dict) -> Base:
        """
        Creates and returns an object of database model.

        Args:
            model_type: Type of model you want to create.
            args: A dictionary containing arguments for object creation.

        Returns:
            An object of a database model.
        """
        model_class = cls.DATABASE_CLASSES_MAPPING.get(model_type)

        if model_class is None:
            raise ValueError(f"Database model '{model_type}' not found.")

        model_instance = model_class(**args)

        return model_instance
