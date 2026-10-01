import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("sql/insurance_claims.db")

# Create cursor
cursor = conn.cursor()

# Read the SQL file
with open("sql/01_fraud_analysis.sql", "r", encoding="utf-8") as file:
    sql_text = file.read()

# Split SQL file into separate queries
queries = [
    query.strip()
    for query in sql_text.split(";")
    if query.strip()
]

# Execute each query separately
for i, query in enumerate(queries, start=1):

    cursor.execute(query)

    # Get the result
    result = cursor.fetchall()

    print(f"\nQuery {i} Result:")

    for row in result:
        print(row)

# Close connection
conn.close()