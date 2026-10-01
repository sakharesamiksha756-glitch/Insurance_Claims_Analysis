import pandas as pd

# ============================================================
# INSURANCE CLAIMS ANALYSIS - EXPLORATORY DATA ANALYSIS
# ============================================================

print("=" * 60)
print("INSURANCE CLAIMS ANALYSIS - EDA")
print("=" * 60)


# ------------------------------------------------------------
# 1. LOAD CLEANED DATA
# ------------------------------------------------------------

input_file = "data/cleaned/fraud_oracle_cleaned.csv"

df = pd.read_csv(input_file)

print("\nDataset loaded successfully.")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ------------------------------------------------------------
# 2. FRAUD SUMMARY
# ------------------------------------------------------------

total_claims = len(df)

fraud_claims = df["FraudFound_P"].sum()

non_fraud_claims = total_claims - fraud_claims

fraud_rate = (fraud_claims / total_claims) * 100


print("\n" + "=" * 60)
print("FRAUD SUMMARY")
print("=" * 60)

print(f"Total Claims: {total_claims}")
print(f"Fraud-Flagged Claims: {fraud_claims}")
print(f"Non-Fraud Claims: {non_fraud_claims}")
print(f"Fraud-Flag Rate: {fraud_rate:.2f}%")


# ------------------------------------------------------------
# 3. FRAUD BY VEHICLE CATEGORY
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY VEHICLE CATEGORY")
print("=" * 60)

vehicle_fraud = (
    df.groupby("VehicleCategory")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

vehicle_fraud["FraudRate"] = vehicle_fraud["mean"] * 100

vehicle_fraud = vehicle_fraud.drop(columns=["mean"])

print(vehicle_fraud)


# ------------------------------------------------------------
# 4. FRAUD BY POLICY TYPE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY POLICY TYPE")
print("=" * 60)

policy_fraud = (
    df.groupby("PolicyType")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

policy_fraud["FraudRate"] = policy_fraud["mean"] * 100

policy_fraud = policy_fraud.drop(columns=["mean"])

print(policy_fraud.sort_values("FraudRate", ascending=False))


# ------------------------------------------------------------
# 5. FRAUD BY DRIVER RATING
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY DRIVER RATING")
print("=" * 60)

driver_rating_fraud = (
    df.groupby("DriverRating")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

driver_rating_fraud["FraudRate"] = (
    driver_rating_fraud["mean"] * 100
)

driver_rating_fraud = driver_rating_fraud.drop(columns=["mean"])

print(driver_rating_fraud)


# ------------------------------------------------------------
# 6. FRAUD BY ACCIDENT AREA
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY ACCIDENT AREA")
print("=" * 60)

area_fraud = (
    df.groupby("AccidentArea")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

area_fraud["FraudRate"] = area_fraud["mean"] * 100

area_fraud = area_fraud.drop(columns=["mean"])

print(area_fraud)


# ------------------------------------------------------------
# 7. FRAUD BY FAULT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY FAULT")
print("=" * 60)

fault_fraud = (
    df.groupby("Fault")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

fault_fraud["FraudRate"] = fault_fraud["mean"] * 100

fault_fraud = fault_fraud.drop(columns=["mean"])

print(fault_fraud)


# ------------------------------------------------------------
# 8. FRAUD BY POLICE REPORT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY POLICE REPORT")
print("=" * 60)

police_report_fraud = (
    df.groupby("PoliceReportFiled")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

police_report_fraud["FraudRate"] = (
    police_report_fraud["mean"] * 100
)

police_report_fraud = police_report_fraud.drop(columns=["mean"])

print(police_report_fraud)


# ------------------------------------------------------------
# 9. FRAUD BY WITNESS PRESENT
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY WITNESS PRESENT")
print("=" * 60)

witness_fraud = (
    df.groupby("WitnessPresent")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

witness_fraud["FraudRate"] = witness_fraud["mean"] * 100

witness_fraud = witness_fraud.drop(columns=["mean"])

print(witness_fraud)


# ------------------------------------------------------------
# 10. FRAUD BY PAST NUMBER OF CLAIMS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY PAST NUMBER OF CLAIMS")
print("=" * 60)

past_claims_fraud = (
    df.groupby("PastNumberOfClaims")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

past_claims_fraud["FraudRate"] = (
    past_claims_fraud["mean"] * 100
)

past_claims_fraud = past_claims_fraud.drop(columns=["mean"])

print(past_claims_fraud)


# ------------------------------------------------------------
# 11. FRAUD BY VEHICLE PRICE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY VEHICLE PRICE")
print("=" * 60)

vehicle_price_fraud = (
    df.groupby("VehiclePrice")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

vehicle_price_fraud["FraudRate"] = (
    vehicle_price_fraud["mean"] * 100
)

vehicle_price_fraud = vehicle_price_fraud.drop(columns=["mean"])

print(vehicle_price_fraud)


# ------------------------------------------------------------
# 12. FRAUD BY AGE OF VEHICLE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FRAUD BY AGE OF VEHICLE")
print("=" * 60)

vehicle_age_fraud = (
    df.groupby("AgeOfVehicle")["FraudFound_P"]
    .agg(["count", "sum", "mean"])
    .reset_index()
)

vehicle_age_fraud["FraudRate"] = (
    vehicle_age_fraud["mean"] * 100
)

vehicle_age_fraud = vehicle_age_fraud.drop(columns=["mean"])

print(vehicle_age_fraud)