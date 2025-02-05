import os
import sqlite3
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(BASE_DIR, "data.csv")
df = pd.read_csv(csv_file)


conn = sqlite3.connect("investments_insights.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS investors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS commitments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id INTEGER NOT NULL,
    asset_class TEXT NOT NULL,
    amount INTEGER NOT NULL,
    FOREIGN KEY (investor_id) REFERENCES investors(id)
);
""")


investor_names = df["Investor Name"].unique()
cursor.executemany(
    "INSERT OR IGNORE INTO investors (name) VALUES (?);",
    [(name,) for name in investor_names]
)

conn.commit()


cursor.execute("SELECT id, name FROM investors;")
investor_mapping = {name: investor_id for investor_id, name in cursor.fetchall()}


commitments_data = [
    (investor_mapping[row["Investor Name"]], row["Commitment Asset Class"], row["Commitment Amount"])
    for _, row in df.iterrows()
]

cursor.executemany(
    "INSERT INTO commitments (investor_id, asset_class, amount) VALUES (?, ?, ?);",
    commitments_data
)

conn.commit()
conn.close()

print("SQLite database setup complete!")
