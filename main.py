from orders_service import OrdersService
from file_parsers.ndjson_file_parser import NDJsonFileParser
from storage_services.sql_alchemy_storage_service import SqlAlchemyStorageService


def main():
    # Load orders from NDJSON file
    data = orders_service.load_and_store_data_from_file("data.ndjson")
    for order in data[:5]:
        print(order)
    print()

    # Get order within time range
    start_timestamp = 99
    end_timestamp = 201
    print(f"Get orders with timestamp between {start_timestamp} and {end_timestamp}")
    results = orders_service.get_orders_in_time_period(99, 201)
    for order in results:
        print(order)
    print()

    # Get users with most ordered products
    num_users = 2
    print(f"Get {num_users} users with most ordered products.")
    results = orders_service.get_users_with_most_ordered_products(num_users)
    for user in results:
        print(user)


if __name__ == "__main__":
    file_parser = NDJsonFileParser()
    storage_service = SqlAlchemyStorageService('sqlite:///database/database.db')
    orders_service = OrdersService(file_parser, storage_service)

    main()
