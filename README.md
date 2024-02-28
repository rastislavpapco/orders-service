# Orders service
This repository contains simple service focused on OOP and relational databases.
The purpose of the orders service is to load data (currently from NDJSON file),
store them in a storage (currently sqlite database) and provide simple queries
for the data (currently get orders in given time period
and get users with most ordered products).

### Installation
`git clone https://github.com/rastislavpapco/orders-service.git`

`cd orders-service`

`python -m venv venv`

`pip install -r requirements.txt`

### Running the service
Simply run main.py - example usage is already prepared there.
Sample database is provided in database/my_database.db, but
you should create a new one when running the service (change path in main.py).