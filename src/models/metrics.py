class MetricsModel():
    def __init__(self, conn):
        self.conn = conn

    def fetch_all(self, options=None):
        sort_clause = ""
        if options is not None and 'sort' in options:
            sort_clause = f" ORDER BY {options['sort']}"

        query = f"SELECT * FROM metrics {sort_clause}"
        cur = self.conn.cursor()
        cur.execute(query)

        rows = cur.fetchall()
        return rows

    def fetch_by_id(self, metric_id):
        cur = self.conn.cursor()
        cur.execute(
            "SELECT * FROM metrics WHERE id = ?", (metric_id))
        row = cur.fetchone()
        return row

    def update_stdev(self, metric):
        sql = """UPDATE metrics
              SET stdev = ?
              WHERE id = ?"""
        cur = self.conn.cursor()
        cur.execute(sql, metric)
        self.conn.commit()

    def update_rank(self, metric):
        sql = """UPDATE metrics
              SET rank = ?
              WHERE id = ?"""
        cur = self.conn.cursor()
        cur.execute(sql, metric)
        self.conn.commit()
