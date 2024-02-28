from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Table, Column
from typing import List

from database.database import Base, User, OrderProduct, Order
from .storage_service import StorageService


class SqlAlchemyStorageService(StorageService):
    """
    Class for storing and querying the data in database through SqlAlchemy.
    """

    def __init__(self, engine_connection_string: str = 'sqlite:///database/my_database.db'):
        # Connect to database and create tables
        self.engine = create_engine(engine_connection_string)
        Base.metadata.create_all(self.engine)

        # Create session maker
        self.Session = sessionmaker(bind=self.engine)
        # Access the database tables
        self.tables = Base.metadata.tables

    # TODO
    def store_data(self, data: List[dict]):
        """
        Stores provided data into the database.

        Args:
            data: Data to store.
        """
        raise NotImplementedError("Storing data is not implemented yet.")

    def _get_table(self, table_name: str) -> Table:
        table = self.tables.get(table_name)
        if table is None:
            raise ValueError(f"Table '{table_name}' doesn't exist.")
        return table

    @staticmethod
    def _get_column(table: Table, column_name: str) -> Column:
        column = table.columns.get(column_name)
        if column is None:
            raise ValueError(f"Column '{column_name}' doesn't exist in table '{table.name}'.")
        return column

    def get_entries_in_range_for_field(self, entity: str, field: str,
                                       lower_bound: float, upper_bound: float) -> List[dict]:
        """
        Queries data from a specified table within a given numerical range.

        Args:
            entity: Name of the table to query.
            field: Name of the column to filter by.
            lower_bound: Lower bound of the numerical range (inclusive).
            upper_bound: Upper bound of the numerical range (inclusive).

        Returns:
            List of dictionaries, each representing a row from the query results.

        Raises:
            ValueError: If table or column don't exist, or if lower bound is greater than upper bound.
        """
        # Get corresponding table and column
        table = self._get_table(entity)
        column = self._get_column(table, field)

        if lower_bound > upper_bound:
            raise ValueError("Lower bound can't be greater than upper bound.")

        with self.Session() as session:
            # Prepare query
            query = session.query(table).filter(column >= lower_bound, column <= upper_bound)

            # Execute the query and transform rows to list of dictionaries
            results = [row._asdict() for row in query.all()]

        return results

    def get_users_with_most_ordered_products(self, num_users: int) -> List[dict]:
        """
        Retrieves a list of users with the most ordered items based on the provided count.

        Args:
            num_users: The number of users to retrieve.

        Returns:
            List of dictionaries, each representing a user and their total purchased item count.
        """
        if num_users < 1:
            raise ValueError("Number of users must be a positive value.")

        with self.Session() as session:
            # Prepare the query
            query = session.query(User, func.count(OrderProduct.product_id).label("num_purchased_products")) \
                .join(Order, User.id == Order.user_id) \
                .join(OrderProduct, Order.id == OrderProduct.order_id) \
                .group_by(User.id) \
                .order_by(func.count(OrderProduct.product_id).desc()) \
                .limit(num_users)

            results = []

            # Execute the query and convert to list of dictionaries
            for row in query.all():
                user_dict = row.User.__dict__
                del user_dict['_sa_instance_state']
                results.append({"user": user_dict, "num_purchased_products": row.num_purchased_products})

        return results
