import pandas as pd
import sqlite3
import os

# ------------------------------------------------------------
# 1. File paths
# ------------------------------------------------------------

csv_path = "data/cleaned/fraud_oracle_cleaned.csv"
db_path = "sql/insurance_claims.db"

# ------------------------------------------------------------
# 2. Check whether cleaned CSV exists
# ------------------------------------------------------------

if not os.path.exists(csv_path):
    print("ERROR: Cleaned CSV file not found.")
    print("Expected location:", csv_path)
    exit()

# ------------------------------------------------------------
# 3. Read cleaned CSV
# ------------------------------------------------------------

df = pd.read_csv(csv_path)

print("CSV loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# ------------------------------------------------------------
# 4. Create SQLite database
# ------------------------------------------------------------

conn = sqlite3.connect(db_path)

# ------------------------------------------------------------
# 5. Store dataframe as SQL table
# ------------------------------------------------------------

df.to_sql(
    "fraud_claims",
    conn,
    if_exists="replace",
    index=False
)

# ------------------------------------------------------------
# 6. Close database connection
# ------------------------------------------------------------

conn.close()

print("\nSQLite database created successfully!")
print("Database:", db_path)
print("Table: fraud_claims")