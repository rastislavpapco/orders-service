from typing import List

from file_parsers.file_parser import FileParser
from storage_services.storage_service import StorageService


class OrdersService:
    """
    This class holds the application logic, which the user should interact with.
    """

    def __init__(self, file_parser: FileParser, storage_service: StorageService):
        self.file_parser = file_parser
        self.storage_service = storage_service

    def load_and_store_data_from_file(self, file_path: str) -> List[dict]:
        """
        Parses data from file and stores them into storage.

        Args:
            file_path (str): The path to the data file.
        """
        orders = self.file_parser.parse_data(file_path)
        # TODO
        # self.storage_service.store_data(orders)
        return orders

    def get_orders_in_time_period(self, time_start: float, time_end: float) -> List[dict]:
        """
        Selects orders in provided time interval.

        Args:
            time_start: Starting time.
            time_end: Ending time.

        Returns:
            List of dictionaries, each representing one order.

        Raises:
            ValueError: If starting time is greater than ending time.
        """
        return self.storage_service.get_entries_in_range_for_field("orders", "created", time_start, time_end)

    def get_users_with_most_ordered_products(self, num_users: int) -> List[dict]:
        """
        Selects users with most ordered products.

        Args:
            num_users: Number of users to retrieve.

        Returns:
            List of dictionaries, each representing a user and their total purchased item count.

        Raises:
            JSONDecodeError: If provided number of users if lower than 1.
        """
        return self.storage_service.get_users_with_most_ordered_products(num_users)
