import json
from typing import List

from .abstract_file_parser import AbstractFileParser


class NDJsonFileParser(AbstractFileParser):
    def parse_data(self, file_path: str) -> List[dict]:
        """
        Parses data from an NDJson file into a list of dictionaries.

        Args:
            file_path (str): The path to the NDJson file to be parsed.

        Returns:
            List[dict]: A list of dictionaries, where each dictionary represents a single order.

        Raises:
            JSONDecodeError: If a line in the file cannot be parsed as valid JSON.
        """
        orders = []

        with open(file_path, 'r') as f:
            for line in f:
                orders.append(json.loads(line.strip()))

        return orders
