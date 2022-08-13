class MetricsPricesModel():
    def __init__(self, conn):
        self.conn = conn

    def count_records(self):
        cur = self.conn.cursor()
        query = "SELECT COUNT(*) FROM metrics_prices"
        cur.execute(query)
        return cur.fetchone()[0]

    def fetch_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM metrics_prices")
        rows = cur.fetchall()
        return rows

    def fetch_all_by_metric_id(self, metric_id, start_date, end_date):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM metrics_prices WHERE metric_id = ? AND created_at BETWEEN ? AND ?",
            (metric_id, start_date, end_date))
        rows = cur.fetchall()
        return rows

    def insert(self, record):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO metrics_prices(metric_id,price,created_at,updated_at) VALUES(?,?,?,?);", record)
        self.conn.commit()
        return cur.lastrowid

    def insert_many(self, rows):
        cur = self.conn.cursor()
        cur.executemany(
            "INSERT INTO metrics_prices(metric_id,price,created_at,updated_at) VALUES(?,?,?,?);", rows)
        self.conn.commit()
        return cur.rowcount
