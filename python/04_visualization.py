import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# INSURANCE CLAIMS ANALYSIS - DATA VISUALIZATION
# ============================================================

print("=" * 60)
print("INSURANCE CLAIMS ANALYSIS - DATA VISUALIZATION")
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
# 2. CALCULATE FRAUD DISTRIBUTION
# ------------------------------------------------------------

fraud_counts = df["FraudFound_P"].value_counts().sort_index()

non_fraud = fraud_counts.get(0, 0)
fraud = fraud_counts.get(1, 0)


# ------------------------------------------------------------
# 3. CREATE FRAUD DISTRIBUTION CHART
# ------------------------------------------------------------

plt.figure(figsize=(8, 6))

bars = plt.bar(
    ["Non-Fraud", "Fraud-Flagged"],
    [non_fraud, fraud]
)

plt.title("Insurance Claim Fraud Distribution")
plt.xlabel("Claim Classification")
plt.ylabel("Number of Claims")

plt.grid(axis="y", alpha=0.3)


# Add values above bars
for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height):,}",
        ha="center",
        va="bottom"
    )


plt.tight_layout()


# ------------------------------------------------------------
# 4. SAVE CHART
# ------------------------------------------------------------

output_file = "images/fraud_distribution.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)
# ============================================================
# 2. FRAUD RATE BY VEHICLE CATEGORY
# ============================================================

vehicle_fraud = (
    df.groupby("VehicleCategory")["FraudFound_P"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))

bars = plt.bar(
    vehicle_fraud.index,
    vehicle_fraud.values
)

plt.title("Fraud Rate by Vehicle Category")
plt.xlabel("Vehicle Category")
plt.ylabel("Fraud Rate (%)")
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_vehicle_category.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)
# ============================================================
# 3. FRAUD RATE BY POLICY TYPE
# ============================================================

policy_fraud = (
    df.groupby("PolicyType")["FraudFound_P"]
    .mean()
    .mul(100)
    .sort_values(ascending=True)
)

plt.figure(figsize=(10, 7))

bars = plt.barh(
    policy_fraud.index,
    policy_fraud.values
)

plt.title("Fraud Rate by Policy Type")
plt.xlabel("Fraud Rate (%)")
plt.ylabel("Policy Type")
plt.grid(axis="x", alpha=0.3)

for bar in bars:
    width = bar.get_width()

    plt.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f" {width:.2f}%",
        ha="left",
        va="center"
    )

plt.tight_layout()

output_file = "images/fraud_rate_policy_type.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)
# ============================================================
# 4. FRAUD RATE BY ACCIDENT AREA
# ============================================================

area_fraud = (
    df.groupby("AccidentArea")["FraudFound_P"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))

bars = plt.bar(
    area_fraud.index,
    area_fraud.values
)

plt.title("Fraud Rate by Accident Area")
plt.xlabel("Accident Area")
plt.ylabel("Fraud Rate (%)")
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_accident_area.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)
# ============================================================
# 5. FRAUD RATE BY FAULT
# ============================================================

fault_fraud = (
    df.groupby("Fault")["FraudFound_P"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))

bars = plt.bar(
    fault_fraud.index,
    fault_fraud.values
)

plt.title("Fraud Rate by Fault")
plt.xlabel("Fault Type")
plt.ylabel("Fraud Rate (%)")
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_fault.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)
# ============================================================
# 6. FRAUD RATE BY DRIVER RATING
# ============================================================

driver_rating_fraud = (
    df.groupby("DriverRating")["FraudFound_P"]
    .mean()
    .mul(100)
    .sort_index()
)

plt.figure(figsize=(8, 6))

bars = plt.bar(
    driver_rating_fraud.index.astype(str),
    driver_rating_fraud.values
)

plt.title("Fraud Rate by Driver Rating")
plt.xlabel("Driver Rating")
plt.ylabel("Fraud Rate (%)")
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_driver_rating.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)

# ============================================================
# 7. FRAUD RATE BY POLICE REPORT
# ============================================================

police_report_fraud = (
    df.groupby("PoliceReportFiled")["FraudFound_P"]
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 6))

bars = plt.bar(
    police_report_fraud.index,
    police_report_fraud.values
)

plt.title("Fraud Rate by Police Report Filed")
plt.xlabel("Police Report Filed")
plt.ylabel("Fraud Rate (%)")
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_police_report.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)

# ============================================================
# 8. FRAUD RATE BY PAST NUMBER OF CLAIMS
# ============================================================

past_claims_fraud = (
    df.groupby("PastNumberOfClaims")["FraudFound_P"]
    .mean()
    .mul(100)
)

# Custom order for easier interpretation
claim_order = [
    "none",
    "1",
    "2 to 4",
    "more than 4"
]

past_claims_fraud = past_claims_fraud.reindex(
    claim_order
)

plt.figure(figsize=(9, 6))

bars = plt.bar(
    past_claims_fraud.index,
    past_claims_fraud.values
)

plt.title("Fraud Rate by Past Number of Claims")
plt.xlabel("Past Number of Claims")
plt.ylabel("Fraud Rate (%)")
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_past_claims.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)

# ============================================================
# 9. FRAUD RATE BY VEHICLE PRICE
# ============================================================

vehicle_price_fraud = (
    df.groupby("VehiclePrice")["FraudFound_P"]
    .mean()
    .mul(100)
)

# Custom order from lowest to highest price
price_order = [
    "less than 20000",
    "20000 to 29000",
    "30000 to 39000",
    "40000 to 59000",
    "60000 to 69000",
    "more than 69000"
]

vehicle_price_fraud = vehicle_price_fraud.reindex(price_order)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    vehicle_price_fraud.index,
    vehicle_price_fraud.values
)

plt.title("Fraud Rate by Vehicle Price")
plt.xlabel("Vehicle Price")
plt.ylabel("Fraud Rate (%)")
plt.xticks(rotation=25)
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_vehicle_price.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)
# ============================================================
# 10. FRAUD RATE BY AGE OF VEHICLE
# ============================================================

age_vehicle_fraud = (
    df.groupby("AgeOfVehicle")["FraudFound_P"]
    .mean()
    .mul(100)
)

# Custom order from newer vehicles to older vehicles
age_vehicle_order = [
    "new",
    "2 years",
    "3 years",
    "4 years",
    "5 years",
    "6 years",
    "7 years",
    "more than 7"
]

age_vehicle_fraud = age_vehicle_fraud.reindex(age_vehicle_order)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    age_vehicle_fraud.index,
    age_vehicle_fraud.values
)

plt.title("Fraud Rate by Age of Vehicle")
plt.xlabel("Age of Vehicle")
plt.ylabel("Fraud Rate (%)")
plt.xticks(rotation=25)
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_vehicle_age.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)

# ============================================================
# 11. FRAUD RATE BY AGE OF POLICY HOLDER
# ============================================================

age_policy_fraud = (
    df.groupby("AgeOfPolicyHolder")["FraudFound_P"]
    .mean()
    .mul(100)
)

age_policy_order = [
    "16 to 17",
    "18 to 20",
    "21 to 25",
    "26 to 30",
    "31 to 35",
    "36 to 40",
    "41 to 50",
    "51 to 65",
    "over 65"
]

age_policy_fraud = age_policy_fraud.reindex(age_policy_order)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    age_policy_fraud.index,
    age_policy_fraud.values
)

plt.title("Fraud Rate by Age of Policy Holder")
plt.xlabel("Age of Policy Holder")
plt.ylabel("Fraud Rate (%)")
plt.xticks(rotation=25)
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_policy_holder_age.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)

# ============================================================
# 12. FRAUD RATE BY NUMBER OF SUPPLEMENTS
# ============================================================

supplements_fraud = (
    df.groupby("NumberOfSuppliments")["FraudFound_P"]
    .mean()
    .mul(100)
)

supplements_order = [
    "none",
    "1 to 2",
    "3 to 5",
    "more than 5"
]

supplements_fraud = supplements_fraud.reindex(supplements_order)

plt.figure(figsize=(9, 6))

bars = plt.bar(
    supplements_fraud.index,
    supplements_fraud.values
)

plt.title("Fraud Rate by Number of Supplements")
plt.xlabel("Number of Supplements")
plt.ylabel("Fraud Rate (%)")
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_supplements.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)

# ============================================================
# 13. FRAUD RATE BY ADDRESS CHANGE
# ============================================================

address_change_fraud = (
    df.groupby("AddressChange_Claim")["FraudFound_P"]
    .mean()
    .mul(100)
)

address_change_order = [
    "no change",
    "under 6 months",
    "1 year",
    "2 to 3 years",
    "4 to 8 years"
]

address_change_fraud = address_change_fraud.reindex(
    address_change_order
)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    address_change_fraud.index,
    address_change_fraud.values
)

plt.title("Fraud Rate by Address Change")
plt.xlabel("Address Change")
plt.ylabel("Fraud Rate (%)")
plt.xticks(rotation=25)
plt.grid(axis="y", alpha=0.3)

for bar in bars:
    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}%",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

output_file = "images/fraud_rate_address_change.png"

plt.savefig(
    output_file,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nChart saved successfully:")
print(output_file)