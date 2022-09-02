# data-tracker

Web service to track crypto data


## Installation

### Requirements
- Linux or macOS or Windows
- Python 3.6+
- SQLite 3
- jq - optional

#### SQLite installation (windows only)
1. Download DLL and binaries (32bits or 64bits) from the download page https://www.sqlite.org/download.html
2. Extract files from zip and run sqlite3.exe to verify it's working in your environment.

#### Project Installation

1. Clone the repo

    `git clone https://github.com/codeandrop/data-tracker.git`

2. cd into the project's folder

    `cd data-tracker`

3. Create a virtual environment

    `python3 -m venv env`

4. Activate the virtual environment

    `source env/bin/activate`

5. Install the project's requirements

    `pip3 install -r requirements.txt`

6. You can run the app by executing

    `python3 main.py`

7. You can leave the virtual env by executing

    `deactivate`

#### Running the tests

1. Follow the instructions to install the project

2. Activate the env if not already

    `source env/bin/activate`

3. The app must be stopped. To run the tests, execute:

    `python3 -m pytest tests/*`


## API Docs

There are 3 endpoints in the app

- `/metrics` - This endpoint will return all metrics stored in the system, it will also return the rank for each metric.

- `/metrics/:metric_id` - This endpoint will return information about a specific metric such as market, base, and quote.

- `/metrics/:metric_id/prices` - This endpoint will return the prices from the last 24 hours of a given metric.


## Usage

- To get all metrics

    `curl "localhost:8888/metrics"`

- To get a specific metric

    `curl "localhost:8888/metrics/1"`

- To get the prices of a metric

    `curl "localhost:8888/metrics/1/prices"`

If you want to improve the response readability, you can use the `jq` command such as:

`curl "localhost:8888/metrics" | jq`


## Architecture

This web API follows an MVC(Model-View-Controller) architecture, it will output information in the JSON format.

There are two main components within the app: metrics and prices.

Metric is a combination of the market (exchange), base, and quote. Additional properties that are tracked include their rank and standard deviation, which are updated every minute via a periodic job.

Prices are information attached to the metric that changes every time period. The default time period for which prices are updated and fetched is one minute.

The periodic job will get the latest prices of all metrics, recalculate their standard deviation, sort by stdev in descending order and update the rank.

Moreover, there is a crypto API service that allows the app to fetch the initial prices on start-up if no prices are stored locally and will fetch the latest price for a given metric.


## Enhancements
- Replace SQLite with PostgreSQL to improve database reliability.
- Add documentation to classes and methods.
- Create a docker container for the app, use the Postgres docker image and use docker-compose to define the interaction between the containers.
- Implement a Task Queue System like Celery or RabbitMQ to handle the periodic updates in the app to better manage failovers and retries.
- Implement periodic metric fetching to allow new metrics to be added to the system.
- Add more unit tests to achieve at least 85% coverage.
- Implement integration tests.
- Use a mock library to test crypto API calls.
- Implement E2E tests.
