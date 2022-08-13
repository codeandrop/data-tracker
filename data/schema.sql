CREATE TABLE metrics (
  id INTEGER PRIMARY KEY,
  market TEXT NOT NULL,
  base TEXT NOT NULL,
  quote TEXT NOT NULL,
  stdev REAL NULL default 0,
  rank INTEGER NULL default 0,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE metrics_prices (
  id INTEGER PRIMARY KEY,
  metric_id INTEGER NOT NULL,
  price REAL NOT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY(metric_id) REFERENCES metrics(id)
);
