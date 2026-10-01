import sqlite3

# Connect to the database
conn = sqlite3.connect("sql/insurance_claims.db")

# Create cursor
cursor = conn.cursor()

# Check total records
cursor.execute("SELECT COUNT(*) FROM fraud_claims")

result = cursor.fetchone()

print("Total records in fraud_claims:", result[0])

# Close connection
conn.close()