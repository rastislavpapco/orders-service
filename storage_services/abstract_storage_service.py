from abc import ABC, abstractmethod
from typing import List


class AbstractStorageService(ABC):
    """
    Class for storing and querying the data.
    """

    @abstractmethod
    def store_data(self, data: List[dict]):
        """
        Stores provided data into the corresponding storage (derived class type).

        Args:
            data: Data to store.
        """
        pass

    @abstractmethod
    def get_entries_in_range_for_field(self, entity: str, field: str,
                                       lower_bound: float, upper_bound: float) -> List[dict]:
        """
        Selects entries from a specified entity within a given numerical range for a field.

        Args:
            entity: Name of the entity (table) to query.
            field: Name of the field (column) to filter by.
            lower_bound: Lower bound of the numerical range (inclusive).
            upper_bound: Upper bound of the numerical range (inclusive).

        Returns:
            List of dictionaries, each representing an entry from the query results.

        Raises:
            ValueError: If entity or field don't exist, or if lower bound is greater than upper bound.
        """
        pass

    @abstractmethod
    def get_users_with_most_ordered_products(self, num_users: int) -> List[dict]:
        """
        Retrieves a list of users with the most ordered items based on the provided count.

        Args:
            num_users: The number of users to retrieve.

        Returns:
            List of dictionaries, each representing a user and their total purchased item count.

        Raises:
            ValueError: If provided number of users is lower than 1.
        """
        pass
