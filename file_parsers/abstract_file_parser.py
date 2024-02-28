from abc import ABC, abstractmethod
from typing import List


class AbstractFileParser(ABC):
    @abstractmethod
    def parse_data(self, file_path: str) -> List[dict]:
        """
        Parses data from a file into a list of dictionaries.

        Args:
            file_path (str): The path to the file to be parsed.

        Returns:
            List[dict]: A list of dictionaries, where each dictionary represents a single order.
        """
        pass
