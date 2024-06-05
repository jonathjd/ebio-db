import sqlite3

conn = sqlite3.connect("db/ebiodata.db")

curr = conn.cursor()

curr.execute(
    """
             CREATE TABLE samples (
             id INTEGER PRIMARY KEY,
             experiment_id TEXT NOT NULL,
             pooling_date DATETIME NOT NULL,
             sample_id TEXT NOT NULL
            )
"""
)


curr.execute(
    "INSERT INTO samples (experiment_id, pooling_date, sample_id) VALUES ('RS086', 2022-12-12, 'RS086_01')"
)
curr.execute(
    "INSERT INTO samples (experiment_id, pooling_date, sample_id) VALUES ('RS125', 2022-12-19, 'RS086_02')"
)
curr.execute(
    "INSERT INTO samples (experiment_id, pooling_date, sample_id) VALUES ('RS334', 2022-12-22, 'RS086_03')"
)

conn.commit()
conn.close()
