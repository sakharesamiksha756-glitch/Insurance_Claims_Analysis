import pandas as pd

# ============================================================
# INSURANCE CLAIMS ANALYSIS - DATA CLEANING
# ============================================================

print("=" * 60)
print("INSURANCE CLAIMS ANALYSIS - DATA CLEANING")
print("=" * 60)

# ------------------------------------------------------------
# 1. LOAD RAW DATA
# ------------------------------------------------------------

input_file = "data/raw/fraud_oracle.csv"

df = pd.read_csv(input_file)

print("\nOriginal dataset shape:")
print(df.shape)


# ------------------------------------------------------------
# 2. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\nMissing values before cleaning:")
print(df.isnull().sum().sum())


# ------------------------------------------------------------
# 3. CHECK DUPLICATES
# ------------------------------------------------------------

print("\nDuplicate rows before cleaning:")
print(df.duplicated().sum())


# ------------------------------------------------------------
# 4. CLEAN VEHICLE PRICE
# ------------------------------------------------------------

vehicle_price_mapping = {
    "less than 20000": 10000,
    "20000 to 29000": 24500,
    "30000 to 39000": 34500,
    "40000 to 59000": 49500,
    "60000 to 69000": 64500,
    "more than 69000": 70000
}

df["VehiclePrice_Numeric"] = df["VehiclePrice"].map(vehicle_price_mapping)


# ------------------------------------------------------------
# 5. CLEAN DAYS POLICY ACCIDENT
# ------------------------------------------------------------

days_policy_accident_mapping = {
    "none": 0,
    "1 to 7": 4,
    "8 to 15": 11.5,
    "15 to 30": 22.5,
    "more than 30": 31
}

df["Days_Policy_Accident_Numeric"] = (
    df["Days_Policy_Accident"]
    .map(days_policy_accident_mapping)
)


# ------------------------------------------------------------
# 6. CLEAN DAYS POLICY CLAIM
# ------------------------------------------------------------

days_policy_claim_mapping = {
    "none": 0,
    "8 to 15": 11.5,
    "15 to 30": 22.5,
    "more than 30": 31
}

df["Days_Policy_Claim_Numeric"] = (
    df["Days_Policy_Claim"]
    .map(days_policy_claim_mapping)
)


# ------------------------------------------------------------
# 7. CLEAN PAST NUMBER OF CLAIMS
# ------------------------------------------------------------

past_claims_mapping = {
    "none": 0,
    "1": 1,
    "2 to 4": 3,
    "more than 4": 5
}

df["PastNumberOfClaims_Numeric"] = (
    df["PastNumberOfClaims"]
    .map(past_claims_mapping)
)


# ------------------------------------------------------------
# 8. CLEAN AGE OF VEHICLE
# ------------------------------------------------------------

age_vehicle_mapping = {
    "new": 0,
    "2 years": 2,
    "3 years": 3,
    "4 years": 4,
    "5 years": 5,
    "6 years": 6,
    "7 years": 7,
    "more than 7": 8
}

df["AgeOfVehicle_Numeric"] = (
    df["AgeOfVehicle"]
    .map(age_vehicle_mapping)
)


# ------------------------------------------------------------
# 9. CLEAN AGE OF POLICY HOLDER
# ------------------------------------------------------------

age_policy_holder_mapping = {
    "16 to 17": 16.5,
    "18 to 20": 19,
    "21 to 25": 23,
    "26 to 30": 28,
    "31 to 35": 33,
    "36 to 40": 38,
    "41 to 50": 45.5,
    "51 to 65": 58,
    "over 65": 66
}

df["AgeOfPolicyHolder_Numeric"] = (
    df["AgeOfPolicyHolder"]
    .map(age_policy_holder_mapping)
)


# ------------------------------------------------------------
# 10. CLEAN NUMBER OF SUPPLEMENTS
# ------------------------------------------------------------

supplements_mapping = {
    "none": 0,
    "1 to 2": 1.5,
    "3 to 5": 4,
    "more than 5": 6
}

df["NumberOfSuppliments_Numeric"] = (
    df["NumberOfSuppliments"]
    .map(supplements_mapping)
)


# ------------------------------------------------------------
# 11. CLEAN ADDRESS CHANGE
# ------------------------------------------------------------

address_change_mapping = {
    "under 6 months": 0.25,
    "1 year": 1,
    "2 to 3 years": 2.5,
    "4 to 8 years": 6,
    "no change": 0
}

df["AddressChange_Claim_Numeric"] = (
    df["AddressChange_Claim"]
    .map(address_change_mapping)
)


# ------------------------------------------------------------
# 12. CLEAN NUMBER OF CARS
# ------------------------------------------------------------

number_cars_mapping = {
    "1 vehicle": 1,
    "2 vehicles": 2,
    "3 to 4": 3.5,
    "5 to 8": 6.5,
    "more than 8": 9
}

df["NumberOfCars_Numeric"] = (
    df["NumberOfCars"]
    .map(number_cars_mapping)
)


# ------------------------------------------------------------
# 13. CHECK CREATED NUMERIC COLUMNS
# ------------------------------------------------------------

numeric_columns_created = [
    "VehiclePrice_Numeric",
    "Days_Policy_Accident_Numeric",
    "Days_Policy_Claim_Numeric",
    "PastNumberOfClaims_Numeric",
    "AgeOfVehicle_Numeric",
    "AgeOfPolicyHolder_Numeric",
    "NumberOfSuppliments_Numeric",
    "AddressChange_Claim_Numeric",
    "NumberOfCars_Numeric"
]

print("\n" + "=" * 60)
print("NEW NUMERIC COLUMNS")
print("=" * 60)

print(df[numeric_columns_created].head())


# ------------------------------------------------------------
# 14. CHECK FOR UNMAPPED VALUES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CHECKING FOR UNMAPPED VALUES")
print("=" * 60)

for column in numeric_columns_created:
    missing_count = df[column].isnull().sum()
    print(f"{column}: {missing_count} unmapped values")


# ------------------------------------------------------------
# 15. FINAL DATA QUALITY CHECK
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FINAL DATA QUALITY CHECK")
print("=" * 60)

print("\nRows:", df.shape[0])
print("Columns:", df.shape[1])
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())


# ------------------------------------------------------------
# 16. SAVE CLEANED DATA
# ------------------------------------------------------------

output_file = "data/cleaned/fraud_oracle_cleaned.csv"

df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("CLEANED DATA SAVED SUCCESSFULLY")
print("=" * 60)

print(f"\nSaved to: {output_file}")