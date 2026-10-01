import pandas as pd

# Load the insurance claims dataset
df = pd.read_csv("data/raw/fraud_oracle.csv")

# Display the first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Display all column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Display data types
print("\nDATA TYPES:")
print(df.dtypes)