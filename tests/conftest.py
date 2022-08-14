import os
import sqlite3
import pytest
from datetime import datetime


def clear_db(conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM metrics_prices")
    cur.execute("DELETE FROM metrics")
    conn.commit()


def insert_metrics(conn):
    metrics_sql = "data/metrics_data.sql"
    cur = conn.cursor()
    with open(os.path.abspath(metrics_sql), encoding="utf-8") as file:
        sql = file.read()
        cur.executescript(sql)
        conn.commit()


def insert_prices(conn):
    prices_sql = "data/prices_data.sql"
    cur = conn.cursor()
    with open(os.path.abspath(prices_sql), encoding="utf-8") as file:
        sql = file.read()
        cur.executescript(sql)
        conn.commit()


@pytest.fixture()
def db_connection():
    database_filepath = "data/test_database.db"

    conn = None
    try:
        conn = sqlite3.connect(os.path.abspath(database_filepath))
    except sqlite3.Error as error:
        print(f"Failed to connect to the database {error}")

    yield conn

    conn.close()


@pytest.fixture()
def load_metrics(db_connection):
    clear_db(db_connection)
    insert_metrics(db_connection)


@pytest.fixture()
def load_prices(db_connection):
    clear_db(db_connection)
    insert_metrics(db_connection)
    insert_prices(db_connection)


@pytest.fixture()
def update_prices_dates(db_connection):
    now = datetime.now().isoformat()
    sql = """UPDATE metrics_prices
              SET created_at = ?
              """
    cur = db_connection.cursor()
    cur.execute(sql, (now,))
    db_connection.commit()
